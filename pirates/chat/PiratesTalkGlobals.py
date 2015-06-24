from direct.gui.DirectGui import *
from pandac.PandaModules import *
from otp.chat.TalkGlobals import *
from pirates.piratesgui import GuiPanel, PiratesGuiGlobals


tpMgr = TextPropertiesManager.getGlobalPtr()

def MC(color, mult):
    returnColor = Vec4(min(color[0] * mult, 1.0), min(color[1] * mult, 1.0), min(color[2] * mult, 1.0), min(color[3] * mult, 1.0))
    return returnColor


def fRange(variable, bottom, top):
    if variable < bottom:
        return bottom
    elif variable > top:
        return top
    else:
        return variable


def TP(light, power, mult = 1.0, add = 0.0):
    lR = fRange(pow(light[0] * mult + add, power), 0.0, 1.0)
    lG = fRange(pow(light[1] * mult + add, power), 0.0, 1.0)
    lB = fRange(pow(light[2] * mult + add, power), 0.0, 1.0)
    lA = light[3]
    poweredLight = Vec4(lR, lG, lB, lA)
    return poweredLight

textMult = 0.34999999999999998
headMult = 1.0
lightTextPow = 0.5
lightHeadPow = 1.0
tpSuper = TextProperties()
tpSuper.setGlyphShift(0.25)
tpSuper.setGlyphScale(2.0)
tpMgr.setProperties('Super', tpSuper)
CPYellow = tpMgr.getProperties('yellow')
CPYellow.setTextColor(*PiratesGuiGlobals.TextFG13)
tpMgr.setProperties('CPYellow', CPYellow)
CPCopperLt = tpMgr.getProperties('gold')
CPCopperLt.setTextColor(*PiratesGuiGlobals.TextLT17)
tpMgr.setProperties('CPCopperLt', CPCopperLt)
CPGoldSlant = tpMgr.getProperties('gold')
CPGoldSlant.setSlant(0.20000000000000001)
tpMgr.setProperties('CPGoldSlant', CPGoldSlant)
CPGoldSlantLt = tpMgr.getProperties('gold')
CPGoldSlantLt.setSlant(0.20000000000000001)
tpMgr.setProperties('CPGoldSlantLt', CPGoldSlantLt)
CPGreenSlant = tpMgr.getProperties('green')
CPGreenSlant.setTextColor(*PiratesGuiGlobals.TextFG19)
CPGreenSlant.setSlant(0.20000000000000001)
tpMgr.setProperties('CPGreenSlant', CPGreenSlant)
CPGreen = tpMgr.getProperties('green')
CPGreen.setTextColor(*PiratesGuiGlobals.TextFG19)
tpMgr.setProperties('CPGreen', CPGreen)
CPPurpleSlant = tpMgr.getProperties('blue')
CPPurpleSlant.setTextColor(*PiratesGuiGlobals.TextFG20)
CPPurpleSlant.setSlant(0.20000000000000001)
tpMgr.setProperties('CPPurpleSlant', CPPurpleSlant)
CPPurple = tpMgr.getProperties('blue')
CPPurple.setTextColor(*PiratesGuiGlobals.TextFG20)
tpMgr.setProperties('CPPurple', CPPurple)
CPRedSlant = tpMgr.getProperties('red')
CPRedSlant.setTextColor(*PiratesGuiGlobals.TextFG6)
CPRedSlant.setSlant(0.20000000000000001)
tpMgr.setProperties('CPRedSlant', CPRedSlant)
CPRed = tpMgr.getProperties('red')
CPRed.setTextColor(*PiratesGuiGlobals.TextFG6)
tpMgr.setProperties('CPRed', CPRed)
CPWhite = tpMgr.getProperties('white')
tpMgr.setProperties('CPWhite', CPWhite)
CPLtBlueLt = tpMgr.getProperties('blue')
CPLtBlueLt.setTextColor(*PiratesGuiGlobals.TextLT5)
tpMgr.setProperties('CPLtBlueLt', CPLtBlueLt)
CPPurpleLt = tpMgr.getProperties('purple')
CPPurpleLt.setTextColor(*PiratesGuiGlobals.TextLT12)
tpMgr.setProperties('CPPurpleLt', CPPurpleLt)
CPOrange = tpMgr.getProperties('orange')
CPOrange.setTextColor(*PiratesGuiGlobals.TextFG11)
tpMgr.setProperties('CPOrange', CPOrange)
CPOrangeSlant = tpMgr.getProperties('orange')
CPOrangeSlant.setTextColor(*PiratesGuiGlobals.TextFG11)
CPOrangeSlant.setSlant(0.20000000000000001)
tpMgr.setProperties('CPOrangeSlant', CPOrangeSlant)
CPMaroon = tpMgr.getProperties('maroon')
CPMaroon.setTextColor(*PiratesGuiGlobals.TextFG15)
tpMgr.setProperties('CPMaroon', CPMaroon)
CPLtGoldLt = tpMgr.getProperties('lightGold')
CPLtGoldLt.setTextColor(*PiratesGuiGlobals.TextLT14)
tpMgr.setProperties('CPLtGoldLt', CPLtGoldLt)
CPYellowHEAD = tpMgr.getProperties('yellow')
CPYellowHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG21, headMult))
tpMgr.setProperties('CPYellowHEAD', CPYellowHEAD)
CPYellowHEAD = tpMgr.getProperties('yellow')
CPYellowHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG21, textMult))
tpMgr.setProperties('CPYellowBODY', CPYellowHEAD)
CPYellowOVER = tpMgr.getProperties('yellow')
CPYellowOVER.setTextColor(*PiratesGuiGlobals.TextFG21)
tpMgr.setProperties('CPYellowOVER', CPYellowOVER)
CPOrangeHEAD = tpMgr.getProperties('orange')
CPOrangeHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG11, headMult))
tpMgr.setProperties('CPOrangeHEAD', CPOrangeHEAD)
CPOrangeHEAD = tpMgr.getProperties('orange')
CPOrangeHEAD.setTextColor(TP(PiratesGuiGlobals.TextLT11, 1.0, 1.0, 0.0))
tpMgr.setProperties('CPOrangeBODY', CPOrangeHEAD)
CPOrangeOVER = tpMgr.getProperties('orange')
CPOrangeOVER.setTextColor(*PiratesGuiGlobals.TextOV11)
tpMgr.setProperties('CPOrangeOVER', CPOrangeOVER)
CPOrangeSlantHEAD = tpMgr.getProperties('orange')
CPOrangeSlantHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG11, headMult))
CPOrangeSlantHEAD.setSlant(0.20000000000000001)
tpMgr.setProperties('CPOrangeSlantHEAD', CPOrangeSlantHEAD)
CPOrangeSlantHEAD = tpMgr.getProperties('orange')
CPOrangeSlantHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG11, textMult))
CPOrangeSlantHEAD.setSlant(0.20000000000000001)
tpMgr.setProperties('CPOrangeSlantBODY', CPOrangeSlantHEAD)
CPGreyHEAD = tpMgr.getProperties('grey')
CPGreyHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG3, headMult, 0.875))
tpMgr.setProperties('CPGreyHEAD', CPGreyHEAD)
CPGreyHEAD = tpMgr.getProperties('grey')
CPGreyHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG3, textMult))
tpMgr.setProperties('CPGreyBODY', CPGreyHEAD)
CPGreyOVER = tpMgr.getProperties('grey')
CPGreyOVER.setTextColor(TP(PiratesGuiGlobals.TextFG3, 1.0, 0.80000000000000004))
tpMgr.setProperties('CPGreyOVER', CPGreyOVER)
CPOrangeSlantOVER = tpMgr.getProperties('orange')
CPOrangeSlantOVER.setTextColor(*PiratesGuiGlobals.TextOV11)
CPOrangeSlantOVER.setSlant(0.20000000000000001)
tpMgr.setProperties('CPOrangeSlantOVER', CPOrangeSlantOVER)
CPCopperHEAD = tpMgr.getProperties('gold')
CPCopperHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG17, headMult))
tpMgr.setProperties('CPCopperHEAD', CPCopperHEAD)
CPCopperHEAD = tpMgr.getProperties('gold')
CPCopperHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG17, textMult))
tpMgr.setProperties('CPCopperBODY', CPCopperHEAD)
CPCopperOVER = tpMgr.getProperties('gold')
CPCopperOVER.setTextColor(*PiratesGuiGlobals.TextOV17)
tpMgr.setProperties('CPCopperOVER', CPCopperOVER)
CPLtBlueHEAD = tpMgr.getProperties('blue')
CPLtBlueHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG5, lightHeadPow))
tpMgr.setProperties('CPLtBlueHEAD', CPLtBlueHEAD)
CPLtBlueHEAD = tpMgr.getProperties('blue')
CPLtBlueHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG5, lightTextPow))
tpMgr.setProperties('CPLtBlueBODY', CPLtBlueHEAD)
CPLtBlueOVER = tpMgr.getProperties('blue')
CPLtBlueOVER.setTextColor(TP(PiratesGuiGlobals.TextFG5, 1.0, 0.80000000000000004))
tpMgr.setProperties('CPLtBlueOVER', CPLtBlueOVER)
CPPurpleHEAD = tpMgr.getProperties('purple')
CPPurpleHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG22, lightHeadPow))
tpMgr.setProperties('CPPurpleHEAD', CPPurpleHEAD)
CPPurpleHEAD = tpMgr.getProperties('purple')
CPPurpleHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG22, lightTextPow))
tpMgr.setProperties('CPPurpleBODY', CPPurpleHEAD)
CPPurpleOVER = tpMgr.getProperties('purple')
CPPurpleOVER.setTextColor(TP(PiratesGuiGlobals.TextFG22, 1.0, 0.80000000000000004))
tpMgr.setProperties('CPPurpleOVER', CPPurpleOVER)
CPLtGoldHEAD = tpMgr.getProperties('lightGold')
CPLtGoldHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG14, headMult))
tpMgr.setProperties('CPLtGoldHEAD', CPLtGoldHEAD)
CPLtGoldHEAD = tpMgr.getProperties('lightGold')
CPLtGoldHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG14, textMult))
tpMgr.setProperties('CPLtGoldBODY', CPLtGoldHEAD)
CPLtGoldOVER = tpMgr.getProperties('lightGold')
CPLtGoldOVER.setTextColor(*PiratesGuiGlobals.TextFG14)
tpMgr.setProperties('CPLtGoldOVER', CPLtGoldOVER)
CPOliveHEAD = tpMgr.getProperties('green')
CPOliveHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG18, lightHeadPow))
tpMgr.setProperties('CPOliveHEAD', CPOliveHEAD)
CPOliveHEAD = tpMgr.getProperties('green')
CPOliveHEAD.setTextColor(TP(PiratesGuiGlobals.TextFG18, lightTextPow))
tpMgr.setProperties('CPOliveBODY', CPOliveHEAD)
CPOliveOVER = tpMgr.getProperties('green')
CPOliveOVER.setTextColor(*PiratesGuiGlobals.TextOV18)
tpMgr.setProperties('CPOliveOVER', CPOliveOVER)
CANNON_DEFENSE = 100
del tpMgr
MESSAGE_COLOR_TABLE = { }
MESSAGE_COLOR_TABLE[TALK_OPEN] = ('CPOrangeHEAD', 'CPGreyHEAD', 'CPOrangeHEAD')
MESSAGE_COLOR_TABLE[TALK_WHISPER] = ('CPOrangeSlantHEAD', 'CPOrangeHEAD', 'CPOrangeSlantHEAD')
MESSAGE_COLOR_TABLE[TALK_ACCOUNT] = ('CPOrangeSlantHEAD', 'CPOrangeHEAD', 'CPOrangeSlantHEAD')
MESSAGE_COLOR_TABLE[TALK_GM] = ('CPPurpleHEAD', 'CPYellowHEAD', 'CPPurpleHEAD')
MESSAGE_COLOR_TABLE[TALK_GUILD] = ('CPLtBlueHEAD', 'CPLtBlueHEAD', 'CPLtBlueHEAD')
MESSAGE_COLOR_TABLE[TALK_PARTY] = ('CPOliveHEAD', 'CPOliveHEAD', 'CPOliveHEAD')
MESSAGE_COLOR_TABLE[TALK_PVP] = ('CPLtGoldHEAD', 'CPLtGoldHEAD', 'CPLtGoldHEAD')
MESSAGE_COLOR_TABLE[AVATAR_THOUGHT] = ('CPOrangeHEAD', 'CPGreyHEAD', 'CPOrangeHEAD')
MESSAGE_COLOR_TABLE[UPDATE_GUILD] = ('CPLtBlueHEAD', 'CPLtBlueHEAD', 'CPLtBlueHEAD')
MESSAGE_COLOR_TABLE[UPDATE_FRIEND] = ('CPOrangeHEAD', 'CPOrangeHEAD', 'CPOrangeHEAD')
MESSAGE_COLOR_TABLE[UPDATE_PARTY] = ('CPOliveHEAD', 'CPOliveHEAD', 'CPOliveHEAD')
MESSAGE_COLOR_TABLE[UPDATE_PVP] = ('CPLtGoldHEAD', 'CPLtGoldHEAD', 'CPLtGoldHEAD')
MESSAGE_COLOR_TABLE[INFO_SYSTEM] = ('CPRed', 'CPRed', 'CPRed')
MESSAGE_COLOR_TABLE[INFO_GAME] = ('CPGreen', 'CPGreen', 'CPGreen')
MESSAGE_COLOR_TABLE[INFO_DEV] = ('CPGreen', 'CPGreen', 'CPGreen')
MESSAGE_COLOR_TABLE[INFO_AVATAR_UNAVAILABLE] = ('CPOrangeHEAD', 'CPOrangeHEAD', 'CPOrangeHEAD')
MESSAGE_COLOR_TABLE[INFO_OPEN] = ('CPOrangeHEAD', 'CPGreyHEAD', 'CPOrangeHEAD')
MESSAGE_COLOR_TABLE[CANNON_DEFENSE] = ('CPLtBlueHEAD', 'CPLtBlueHEAD', 'CPLtBlueHEAD')
MESSAGE_COLOR_TABLE[INFO_GUILD] = ('CPLtBlueHEAD', 'CPLtBlueHEAD', 'CPLtBlueHEAD')
MESSAGE_OVER_TABLE = { }
MESSAGE_OVER_TABLE[TALK_OPEN] = ('CPOrangeOVER', 'CPGreyOVER', 'CPOrangeOVER')
MESSAGE_OVER_TABLE[TALK_WHISPER] = ('CPOrangeSlantOVER', 'CPOrangeOVER', 'CPOrangeSlantOVER')
MESSAGE_OVER_TABLE[TALK_ACCOUNT] = ('CPOrangeSlantOVER', 'CPOrangeOVER', 'CPOrangeSlantOVER')
MESSAGE_OVER_TABLE[TALK_GM] = ('CPPurpleOVER', 'CPYellowOVER', 'CPPurpleOVER')
MESSAGE_OVER_TABLE[TALK_GUILD] = ('CPLtBlueOVER', 'CPLtBlueOVER', 'CPLtBlueOVER')
MESSAGE_OVER_TABLE[TALK_PARTY] = ('CPOliveOVER', 'CPOliveOVER', 'CPOliveOVER')
MESSAGE_OVER_TABLE[TALK_PVP] = ('CPLtGoldOVER', 'CPLtGoldOVER', 'CPLtGoldOVER')
MESSAGE_OVER_TABLE[AVATAR_THOUGHT] = ('CPOrangeOVER', 'CPGreyOVER', 'CPOrangeOVER')
MESSAGE_OVER_TABLE[UPDATE_GUILD] = ('CPLtBlueOVER', 'CPLtBlueOVER', 'CPLtBlueOVER')
MESSAGE_OVER_TABLE[UPDATE_FRIEND] = ('CPOrangeOVER', 'CPOrangeOVER', 'CPOrangeOVER')
MESSAGE_OVER_TABLE[UPDATE_PARTY] = ('CPOliveOVER', 'CPOliveOVER', 'CPOliveOVER')
MESSAGE_OVER_TABLE[UPDATE_PVP] = ('CPLtGoldOVER', 'CPLtGoldOVER', 'CPLtGoldOVER')
MESSAGE_OVER_TABLE[INFO_SYSTEM] = ('CPRed', 'CPRed', 'CPRed')
MESSAGE_OVER_TABLE[INFO_GAME] = ('CPGreen', 'CPGreen', 'CPGreen')
MESSAGE_OVER_TABLE[INFO_DEV] = ('CPGreen', 'CPGreen', 'CPGreen')
MESSAGE_OVER_TABLE[INFO_AVATAR_UNAVAILABLE] = ('CPOrangeOVER', 'CPOrangeOVER', 'CPOrangeOVER')
MESSAGE_OVER_TABLE[INFO_OPEN] = ('CPOrangeHEAD', 'CPGreyOVER', 'CPOrangeHEAD')
MESSAGE_OVER_TABLE[CANNON_DEFENSE] = ('CPLtBlueOVER', 'CPLtBlueOVER', 'CPLtBlueOVER')
MESSAGE_OVER_TABLE[INFO_GUILD] = ('CPLtBlueOVER', 'CPLtBlueOVER', 'CPLtBlueOVER')
MESSAGE_STYLE_TABLE = { }
MESSAGE_STYLE_TABLE[TALK_OPEN] = ('CPWhite', 'CPGreyBODY', 'CPOrangeHEAD')
MESSAGE_STYLE_TABLE[TALK_WHISPER] = ('CPWhite', 'CPOrangeBODY', 'CPOrangeHEAD')
MESSAGE_STYLE_TABLE[TALK_ACCOUNT] = ('CPWhite', 'CPOrangeBODY', 'CPOrangeHEAD')
MESSAGE_STYLE_TABLE[TALK_GM] = ('CPWhite', 'CPYellowBODY', 'CPPurpleHEAD')
MESSAGE_STYLE_TABLE[TALK_GUILD] = ('CPWhite', 'CPLtBlueBODY', 'CPLtBlueHEAD')
MESSAGE_STYLE_TABLE[TALK_PARTY] = ('CPWhite', 'CPOliveBODY', 'CPOliveHEAD')
MESSAGE_STYLE_TABLE[TALK_PVP] = ('CPWhite', 'CPLtGoldBODY', 'CPLtGoldHEAD')
MESSAGE_STYLE_TABLE[AVATAR_THOUGHT] = ('CPWhite', 'CPGreyBODY', 'CPOrangeHEAD')
MESSAGE_STYLE_TABLE[UPDATE_GUILD] = ('CPLtBlueHEAD', 'CPLtBlueBODY', 'CPLtBlueHEAD')
MESSAGE_STYLE_TABLE[UPDATE_FRIEND] = ('CPOrangeHEAD', 'CPOrangeBODY', 'CPOrangeHEAD')
MESSAGE_STYLE_TABLE[UPDATE_PARTY] = ('CPOliveHEAD', 'CPOliveBODY', 'CPOliveHEAD')
MESSAGE_STYLE_TABLE[UPDATE_PVP] = ('CPLtGoldHEAD', 'CPGLtGoldBODY', 'CPLtGoldHEAD')
MESSAGE_STYLE_TABLE[INFO_SYSTEM] = ('CPRed', 'CPRed', 'CPRed')
MESSAGE_STYLE_TABLE[INFO_GAME] = ('CPGreen', 'CPGreen', 'CPGreen')
MESSAGE_STYLE_TABLE[INFO_DEV] = ('CPGreen', 'CPGreen', 'CPGreen')
MESSAGE_STYLE_TABLE[INFO_AVATAR_UNAVAILABLE] = ('CPOrange', 'CPOrangeBODY', 'CPOrange')
MESSAGE_STYLE_TABLE[INFO_OPEN] = ('CPOrangeHEAD', 'CPGreyBODY', 'CPOrangeHEAD')
MESSAGE_STYLE_TABLE[CANNON_DEFENSE] = ('CPWhite', 'CPLtBlueBODY', 'CPLtBlueHEAD')
MESSAGE_STYLE_TABLE[INFO_GUILD] = ('CPLtBlue', 'CPLtBlueBODY', 'CPLtBlueHEAD')
