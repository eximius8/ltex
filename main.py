mytext = mytext.replace('Ƥ', 'P')
mytext = mytext.replace('Ɗ', 'D')
mytext = mytext.replace('µ', '\mu ')
mytext = mytext.replace('ℱ', 'F')
mytext = mytext.replace('≡', '\equiv')
mytext = mytext.replace('→', '\rightarrow')



mytext = mytext.replace('⊇', '\supseteq')
mytext = mytext.replace('…', '\ldots')
mytext = mytext.replace('⸦', '\subset')
mytext = mytext.replace('ϵ', '\in')
mytext = mytext.replace('DnR', 'D_{nR}')
mytext = mytext.replace('∃', '\exists')
mytext = mytext.replace('D1R', 'D_{1R}')




for i in range(22, 0, -1):
    for j in range(22, 0, -1):
        for Letter in ['F', 'E', 'D']:
            mytext = mytext.replace(f'{Letter}{i},{j}', f'{Letter}_' + '{' + f'{i},{j}' + '}')
            
        for k in range(22, 0, -1):
            mytext = mytext.replace(f'({i}.{j}.{k})', '\eqref{eq:' + f'{i}{j}{k}' + '}')
            for l in range(22, 0, -1):
                mytext = mytext.replace(f'({i}.{j}.{k}.{l})', '\eqref{eq:' + f'{i}{j}{k}{l}' + '}')
for Main in ['F', 'E']:
    for ind in ['i', 'j', 'k']:
        for sind in ['i', 'j', 'k']:
            mytext = mytext.replace(f'{Main}{ind},{sind}', f'{Main}_' + '{' + f'{ind},{sind}' + '}'  )
            mytext = mytext.replace(f'{Main}{ind}{sind}', f'{Main}_' + '{' + f'{ind}{sind}' + '}'  )

for Main in ['F', 'E', 'D']:
    for ind in ['i', 'j', 'k', 'n', '1', 'm']:
        mytext = mytext.replace(f'{Main}{ind}', f'{Main}_' + '{' + f'{ind}' + '}'  )
print(mytext)
