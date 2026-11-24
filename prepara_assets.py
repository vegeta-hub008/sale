#!/usr/bin/env python3
"""Esegui UNA volta (doppio click o `python prepara_assets.py`) nella cartella che contiene index.html e assets/.
Crea assets/pack/*.js cosi' index.html funziona anche con doppio click (file://)."""
import os,re,base64
root=os.path.dirname(os.path.abspath(__file__));out=os.path.join(root,'assets','pack');os.makedirs(out,exist_ok=True);n=0
for d,_,fs in os.walk(os.path.join(root,'assets')):
    if os.path.abspath(d).startswith(os.path.abspath(out)):continue
    for f in fs:
        if not f.lower().endswith(('.glb','.webp','.jpg','.jpeg','.png')):continue
        rel=os.path.relpath(os.path.join(d,f),root).replace(os.sep,'/')
        b=base64.b64encode(open(os.path.join(d,f),'rb').read()).decode()
        open(os.path.join(out,re.sub(r'[^A-Za-z0-9._-]','_',rel)+'.js'),'w').write('window.__PK=window.__PK||{};__PK[%r]="%s";'%(rel,b));n+=1
print('Creati',n,'file in assets/pack')
