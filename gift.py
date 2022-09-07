
import random
import time
def CheckNumberRepeat(yl, zy, xx, ll):
    if yl in {zy,xx,ll}:
        return False
    elif zy in {xx,ll}:
        return False
    elif xx==ll:
        return False
    else:
        return True

def GenerateUnRepeatedNumber():
    Repeated = True
    yl = 0
    zy = 0
    xx = 0
    ll = 0
    while Repeated:
        yl = random.randint(1,4)
        zy = random.randint(1,4)
        xx = random.randint(1,4)
        ll = random.randint(1,4)
        if (CheckNumberRepeat(yl, zy, xx, ll)):
            Repeated = False
    return yl, zy, xx, ll

def CheckMineGift(yl, zy, xx, ll, ylPick, zyPick, xxPick, llPick):
    if( yl == ylPick or zy == zyPick or xx == xxPick or ll==llPick):
        return False
    else:
        return True

def GiftToName(GiftNumber, yl, zy, xx, ll):
    if GiftNumber == yl:
        return "yl"
    if GiftNumber==zy:
        return "zy"
    if GiftNumber == xx:
        return "xx"
    if GiftNumber == ll:
        return "ll"

if __name__ == '__main__':

    yl, zy, xx, ll = GenerateUnRepeatedNumber()

    print("***********Gift Number***********\n")
    print("*\tyl gift number:  %d\t* \n" % yl)
    print("*\tzy gift number:  %d\t* \n" % zy)
    print("*\txx gift number:  %d\t* \n" % xx)
    print("*\tll gift number:  %d\t* \n" % ll)
    print("*********************************\n")

    time.sleep(5)
    Ready = False
    while(not Ready):
        ylPick, zyPick, xxPick, llPick = GenerateUnRepeatedNumber()
        print(".")
        time.sleep(1)
        Ready = CheckMineGift(yl, zy, xx, ll, ylPick, zyPick, xxPick, llPick)

    print("gift assign success!")

    print("%d,%d,%d,%d"%(ylPick, zyPick, xxPick, llPick))
    print("***********Gift Assign***********\n")
    print("*\tyl Pick %s gift \t* \n" % GiftToName(ylPick, yl, zy, xx, ll))
    print("*\tzy Pick %s gift \t* \n" % GiftToName(zyPick, yl, zy, xx, ll))
    print("*\txx Pick %s gift \t* \n" % GiftToName(xxPick, yl, zy, xx, ll))
    print("*\tll Pick %s gift \t* \n" % GiftToName(llPick, yl, zy, xx, ll))
    print(" ********************************\n")



