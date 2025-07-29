from datetime import datetime
import math

dateTimeObj = datetime.now()

total = []
totalx = []
totaly = []
totala = []
totalb = []
totalf = []
totald = []
jumlaha1 = []
jumlaha2 = []
jumlaha3 = []
jumlaha4 = []
jumlaha5 = []
jumlaha6 = []
custom = []
flx = []
pp = []
cbga = []
cbgm = []
name = []
char1 = []
char2 = []
char3 = []
char4 = []
char5 = []
char6 = []
disco = []
disask = []
nom = []

def harga():
    print('=' * 25, 'PRICES', '=' * 25)
    print('')
    print('1. Feral vehicle drawing w/ flat/gradient bg USD 6')
    print('2. Feral vehicle headshot w/ flat/gradient bg USD 3')
    print('3. Humanoid drawing w/ flat/gradient bg      USD 8.5')
    print('4. Humanoid headshot w/ flat/gradient bg USD 5')
    print('5. Joyflight/Seat Hug YCH                    USD 10')
    print('6. A4 Doodles                                USD 5')
    print('')
    print('Addons:')
    print('1. Change bg to custom bg                    USD 2.5')
    print('2. Flex that feral                           USD 2')
    print('')
    print('NOTE: PRICES ARE PER CHARACTER')
    print('NOTE: PAYPAL PROCESSING FEE USD 1')
    print('')
    nama()

def nama():
    print('=' * 25, '======', '=' * 25)
    print('')
    person = str(input('Customer               : '))
    name.append(person)
    nomoe = int(input('Order Number           : '))
    nom.append(nomoe)
    kasir()
    return

def kasir():
    custom_bg = float(2.5)
    kode = int(input('Input item             : '))

    if kode == 1:
        print('Feral vehicle drawing')
        jumlah1 = int(input('Number of characters   : '))
        jumlaha1.append(jumlah1)
        for i in range(0, jumlah1):
            oc1 = str(input('Character: '))
            char1.append(oc1)
        total1 = jumlah1 * 6
        customf = str(input('Does the feral flex?(y/n)        : '))
        flx.append(customf)
        if customf =='y':
            total1 = total1 + (jumlah1 * 2)
            print('Total amount for feral + flex: USD', total1)
        elif customf == 'n':
            print('Total amount for feral: USD', total1)
        else:
            print('Wrong input')
            kasir()
        totalx.append(total1)
        total.append(total1)
        print('')
        tanya()

    elif kode == 2:
        print('Feral vehicle headshot')
        jumlah2 = int(input('Number of characters   : '))
        jumlaha2.append(jumlah2)
        for i in range(0, jumlah2):
            oc2 = str(input('Character: '))
            char2.append(oc2)
        total2 = jumlah2 * 3
        print('Total amount for fvehicle head: USD', total2)
        totaly.append(total2)
        total.append(total2)
        print('')
        tanya()

    elif kode == 3:
        print('Humanoid drawing')
        jumlah3 = int(input('Number of characters   : '))
        jumlaha3.append(jumlah3)
        for i in range(0, jumlah3):
            oc3 = str(input('Character: '))
            char3.append(oc3)
        total3 = jumlah3 * 8.5
        print('Total amount for humanoid drawing: USD', total3)
        totala.append(total3)
        total.append(total3)
        print('')
        tanya()

    elif kode == 4:
        print('Humanoid headshot')
        jumlah4 = int(input('Number of characters   : '))
        jumlaha4.append(jumlah4)
        for i in range(0, jumlah4):
            oc4 = str(input('Character: '))
            char4.append(oc4)
        total4 = jumlah4 * 5
        print('Total amount for humanoid head: USD', total4)
        totalb.append(total4)
        total.append(total4)
        print('')
        tanya()

    elif kode == 5:
        print('Joyflight/Seat Hug YCH')
        jumlah5 = int(input('Number of characters   : '))
        jumlaha5.append(jumlah5)
        for i in range(0, jumlah5):
            oc5 = str(input('Character: '))
            char5.append(oc5)
        total5 = jumlah5 * 10
        print('Total amount for Joyflight/Seat Hug YCH: USD', total5)
        totalf.append(total5)
        total.append(total5)
        print('')
        tanya()
        
    elif kode == 6:
        print('A4 Doodles')
        jumlah6 = int(input('Number of characters   : '))
        jumlaha6.append(jumlah6)
        for i in range(0, jumlah6):
            oc6 = str(input('Character: '))
            char6.append(oc6)
        total6 = jumlah6 * 5
        print('Total amount for A4 Doodles: USD', total6)
        totald.append(total6)
        total.append(total6)
        print('')
        tanya()

    else:
        print('Wrong input')
        kasir()

    return

def tanya():
    tanyaa = str(input('Add more items?(y/n)      : '))
    if tanyaa =='y':
        print('')
        kasir()
    elif tanyaa == 'n':
        print('')
        tanya_custom()
    else:
        print('Wrong input')
        tanya()
    return

def tanya_custom():
    tcus = str(input('Custom background?(y/n)   : '))
    cbga.append(tcus)
    if tcus =='y':
        tcusmany = int(input('For how many separate drawings?: '))
        totalcus = tcusmany * 2.5
        cbgm.append(tcusmany)
        print('Total custom background(s): USD', totalcus)
        print('')
        custom.append(totalcus)
        total.append(totalcus)
        tanya_paypal()
    elif tcus =='n':
        print('')
        tanya_paypal()
    else:
        print('Wrong input')
        tanya_custom()
    return

def tanya_paypal():
    paypal = float(1)
    tpay = str(input('Use paypal?(y/n)          : '))
    pp.append(tpay)
    if tpay =='y':
        print('')
        total.append(paypal)
        diskon()
    elif tpay == 'n':
        print('')
        diskon()
    else:
        print('Wrong input')
        tanya_paypal()

def diskon():
    distanya = str(input('Discount?(y/n)            : '))
    disask.append(distanya)
    if distanya == 'y':
        discount = float(input('Input discount            : '))
        disco.append(discount)
        akhir()
    elif distanya == 'n':
        akhir()
    else:
        print('Wrong input')
        diskon()
    return

def akhir():
    print('')
    print('=' * 25, 'RECEIPT', '=' * 25)
    print('')
    print('Order Number :', *nom)
    print('')
    print('Date of order:',dateTimeObj)
    print('')
    print('Customer     :', *name)
    print('')
    print('Item                                       Quant.    Cost')
    print('-----------------------------------------------------------')
    if(sum(jumlaha1))>=1:
        if 'y' in flx:
            print('Feral vehicle drawing + flex                 x',sum(jumlaha1) ,'USD',sum(totalx))
        else:
            print('Feral vehicle drawing                        x',sum(jumlaha1) ,'USD',sum(totalx))
        print('Characters:')
        print('\n'.join(char1))
        print('')
    if(sum(jumlaha2))>=1:
        print('fvehicle headshot                            x',sum(jumlaha2) ,'USD',sum(totaly))
        print('Characters:')
        print('\n'.join(char2))
        print('')
    if(sum(jumlaha3))>=1:
        print('humanoid drawing                             x',sum(jumlaha3) ,'USD',sum(totala))
        print('Characters:')
        print('\n'.join(char3))
        print('')
    if(sum(jumlaha4))>=1:
        print('humanoid headshot                            x',sum(jumlaha4) ,'USD',sum(totalb))
        print('Characters:')
        print('\n'.join(char4))
        print('')
    if sum(jumlaha5) >= 1:
        print('Joyflight/Seat Hug YCH                       x', sum(jumlaha5), 'USD', sum(totalf))
        print('Characters:')
        print('\n'.join(char5))
        print('')
    if sum(jumlaha6) >= 1:
        print('A4 Doodles                                   x', sum(jumlaha6), 'USD', sum(totald))
        print('Characters:')
        print('\n'.join(char6))
        print('')
    if 'y' in cbga:
        print('Custom background(s)                         x',sum(cbgm) ,'USD',sum(custom))
    if 'y' in pp:
        print('Paypal processing fee                            USD 1.0')
    if 'y' in disask:
        print('Discount                                         USD', sum(disco))
    print('-----------------------------------------------------------')
    print('                                     Total cost: USD',sum(total)-sum(disco))
    print('                                                           ')
    print('                               Thank you for your purchase!')
    print('                        And tips are greatly appreciated ;3')
    
harga()
