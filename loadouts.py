from abc import *

class Loadouts(metaclass=ABCMeta):
    def __init__(self,fpm,dicem):
        self.__fpm=fpm
        self.__dicem=dicem

    @property
    def pointdefencedamage(self):
        pass

    @property
    def fpm(self):
        return self.__fpm
    @property
    def defencedice(self):
        return self.__dicem

    @property
    def showspecificoptions(self):
        pass

    @property
    def modifyfp(self):
        pass

    @property
    def defencepool(self):
        pass

    @property
    def modifysuccess(self,n):
        pass



class Light_MAC(Loadouts):
    def __init__(self):
        super().__init__(self,fpm=0,dicem=0)
        self.__macvalue=1

    @property
    def MacValue(self):
        return self.__macvalue

    @property
    def __str__(self):
        return "Light MAC(1)"


class Heavy_MAC(Loadouts):
    def __init__(self):
        super().__init__(self, fpm=0, dicem=0)
        self.__macvalue=2

    @property
    def MacValue(self):
        return self.__macvalue

    @property
    def __str__(self):
        return "Heavy MAC(2)"



class Missile_Weapon(Loadouts):
    def __init__(self):
        super().__init__(self, fpm=1, dicem=0)

    @property
    def modifyfp(self,LongRange):
        if LongRange==True:
            return fpm

    @property
    def __str__(self):
        return "Missile Weapon"



class Glide(Loadouts):
    def __init__(self,d):
        super().__init__(self,fpm=0,dicem=0)
        self.__gliderange=d
    @property
    def GlideRange(self):
        return self.__gliderange

    @property
    def __str__(self):
        return "Glide"

class Hard_Burn(Loadouts):
    def __init__(self,d):
        super().__init__(self,fpm=0,dicem=0)
        self.__BurnRange=d
    @property
    def BurnRange(self):
        return self.__BurnRange

    @property
    def __str__(self):
        return "Hard Burn"

class Lumbering(Loadouts):
    def __init__(self):
        super().__init__(self,fpm=0,dicem=0)


    @property
    def __str__(self):
        return "Lumbering"

class Nimble(Loadouts):
    def __init__(self):
        super().__init__(self,fpm=0,dicem=0)


    @property
    def __str__(self):
        return "Nimble"

class Cloaking_System(Loadouts):
    def __init__(self):
        super().__init__(self, fpm=-1, dicem=0)

    @property
    def modifyfp(self,LongRange):
        if LongRange == True:
            return fpm

    @property
    def __str__(self):
        return "Cloaking System"

class Defence_Array(Loadouts):
    def __init__(self,n):
        super().__init__(self,fpm=0,dicem=0)
        self.__ArrayValue=n

    @property
    def ArrayValue(self):
        return self.__ArrayValue
    @property
    def defencedicepool(self):
        dicem=misc.Damage_Dice_Roll(self.__ArrayValue,4)
        return dicem

    @property
    def __str__(self):
        return "Defence Array({})".format(self.__ArrayValue)

class Elusive(Loadouts):
    def __init__(self):
        super().__init__(self,fpm=-1,dicem=0)
    @property
    def __str__(self):
        return "Elusive"

    @property
    def modifyfp(self):
        return fpm

class Hard_Target():
    def __init__(self):
        super().__init__(self, fpm=-1, dicem=0)

    @property
    def __str__(self):
        return "Hard Target"
    @property
    def modifysuccess(self,n):
        return -n

class Massive():
    def __init__(self):
        None
    def modifyfp(self,LongRange):
        if LongRange==False:
            return -1


    @property
    def __str__(self):
        return "Massive"

class Missile_Barrage():
    def __init__(self):
        None

    @property
    def __str__(self):
        return "Missile Barrage"


class Plasma_Weapon():
    def __init__(self):
        None

    @property
    def modifyfp(self,d):
        if d>self.__ShortRange:
            return -1
        else:
            return +1

    @property
    def __str__(self):
        return "Plasma Weapon"

class Beam(Plasma_Weapon):
    def __init__(self):
        super().__init__()

    @property
    def __str__(self):
        return "Plasma Beam"

    @property
    def showspecificoptions(self):
        return "Plasma Beam Attack"

class Plasma_Cannon_Array(Plasma_Weapon):
    def __init__(self):
        super().__init__()

    @property
    def __str__(self):
        return "Plasma Cannon Array"

class Plasma_Torpedoes(Plasma_Weapon):
    def __init__(self):
        super().__init__()

    @property
    def modifyfp(self,d):
        if d>=self.__ShortRange:
            return 0
        else:
            return -1

    @property
    def __str__(self):
        return "Plasma Torpedoes"

class Plasma_Lance(Plasma_Weapon):
    def __init__(self):
        super().__init__()

    @property
    def __str__(self):
        return "Plasma Lance"

class Point_Defence():
    def __init__(self,n):
        self.__Point_Value=n
    @property
    def Point_Value(self):
        return self.__Point_Value

    @property
    def pointdefencedamage(self):
        return misc.Damage_Dice_Roll(self.__Point_Value,4)


    @property
    def __str__(self):
        return "Point Defence({})".format(self.__Point_Value)

class Titanium_Armor():
    def __init__(self,n):
        self.__Armor_Value=n
    @property
    def ArmorValue(self):
        return self.__Armor_Value
    @property
    def defencedicepool(self):
        return misc.Damage_Dice_Roll(self.__Armor_Value,4)

    @property
    def __str__(self):
        return "Titanium Armor({})".format(self.__Armor_Value)

class Carrier_Action():
    def __init__(self,n):
        self.__Carrier_Value=n
    @property
    def Carrier_Value(self):
        return self.__Carrier_Value

    @property
    def __str__(self):
        return "Carrier Action({})".format(self.__Carrier_Value)


class Emplacement():
    def __init__(self):
        None

    @property
    def __str__(self):
        return "Emplacement"








