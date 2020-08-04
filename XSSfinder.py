import click
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm

@click.command()
@click.option('-f','--file')
@click.option('-m','--mark')
@click.option('-p','--payload')
@click.option('-o','--output')
def main(file,mark,output,payload):
    f=open(file,"r")
    if(output is not None):
        o=open(output,"w")
    if(mark is None):
        mark="patataman"
    if(payload is not None):
        p=open(payload,"r")
    else:
        print("[+] Utilitzant payloads per defecte.")
        p=open("xssTest.txt","r")
    pls=[]
    for pl in p:
        pls.append(pl)
    options = Options()
    options.add_argument('--headless')
    count=len(f.readlines())
    f.seek(0)

    for url in tqdm(f,total=count,desc="Processant: ",unit="URLs"):
        for pl in pls:
            try:
                driver=webdriver.Firefox(options=options)
                location=url.replace(mark,pl)
                driver.get(location)
                obj= None
                obj = driver.switch_to.alert
                if(obj.text is not None):
                    tqdm.write(location)
                    if(output is not None):
                        o.write(location)
                    obj.accept()
                    break
                else:
                    XSS=False
            except:
                XSS=False
            finally:
                driver.quit()

    p.close()
    f.close()
    if(output is not None):
        o.close()

if(__name__=='__main__'):
    main()
