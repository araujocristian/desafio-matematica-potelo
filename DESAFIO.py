num_ent = int(input("Numero de Entradas: "))
if(0<num_ent<100):
    x=0
    lis_final=[]
    while x<num_ent:

        srt_ent = input("Escreva Aqui: ") #pede uma entrada
        srt_inv = srt_ent.split()[::-1] #transforma a frase em lista, ja em ondem invertida
        if (0<len(srt_inv)<100): #verifica se há menos de 100 palavras
            num_pal = len(srt_inv) #pega a quantidade de palavras
            i=0
            while i<num_pal: #enquanto i for menor que a quantidade de palavras
                if(0<len(srt_inv[i])<30): #verifica se a palavra tem tamanho menor de 30
                    if (srt_inv[i].isdigit()):
                        srt_inv = ['MATEMATICA']
                    
                    i=i+1
                else:
                    print ('PALAVRA MUITO GRANDE')
        else:
                print('NUMERO MAXIMO DE PALAVRAS EXECIDO')

        lis_final.append(srt_inv)
        x=x+1
    for x in lis_final:
        print (" ".join(x))
else:
    print("NUMERO DE ENTRADAS INVALIDO")
    

