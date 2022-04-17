import os
import sys
import zipfile as zip
import zlib

#Each '\' needs to be doubled for reason I can no longer remember
install_path = "C:\\Spel\\DCS World\\"
#Installed aircraft
#Attack
a10c = True
a10c2 = True
av8b = True
ajs37 = True
#WWII
bf109 = True
fw190a = True
fw190d = True
p51 = True
p47 = True
spitfire = True
#Korea
f86 = True
mig15 = True
#Trainer
l39 = True
c101 = True
#Modern
f18 = True
f16 = True
f14 = False
jf17 = True
m2000 = True
#MiG-21 can be left at false, skins already unlocked and zipped files takes ages to process
mig21 = False
f5 = True
#Heli
ah64 = True
mi24 = True
mi8 = True
uh1 = True
ka50 = True
sa342 = True
#FC3
a10a = True
f15 = True
su25 = True
su25t = True
su27 = True
su33 = True
mig29 = True
#other
christeneagle = True
yak52 = True
tf51 = True

def main():
    print("Wiping countries of the drive")
    listed_aircraft = get_all_aircraft()
    path = install_path
    first_part = "CoreMods\\aircraft\\"
    first_aircraft = listed_aircraft[0]
    for aircraft in first_aircraft:
        for model in first_aircraft[aircraft]:
            this_path = path + first_part + aircraft + "\\Liveries\\" + model + "\\"
            clear_countries(this_path)

    second_part = "Bazar\\Liveries\\"
    second_aircraft = listed_aircraft[1]
    for aircraft in second_aircraft:
        this_path = path + second_part + aircraft + "\\"
        clear_countries(this_path)
    third_part = "CoreMods\\WWII Units\\"
    third_aircraft = listed_aircraft[2]
    for aircraft in third_aircraft:
        for model in third_aircraft[aircraft]:
            this_path = path + third_part + aircraft + "\\Liveries\\" + model + "\\"
            clear_countries(this_path)
    fourth_part = "CoreMods\\aircraft\\"
    fourth_aircraft = listed_aircraft[3]
    for aircraft in fourth_aircraft:
        for model in fourth_aircraft[aircraft]:
            this_path = path + fourth_part + aircraft + "\\Liveries\\" + model + "\\"
            clear_countries(this_path)
            

    print("All done!")
def get_all_aircraft():
    coremods = {}
    bazar = {}
    wwii = {}
    zip = {}

    #Attack
    if(a10c):
        #"A-10" : {"A-10C", "A-10A", "A-10CII"}
        if "A-10" in coremods:
            orig = coremods.get("A-10")
            orig.add("A-10C")
            coremods["A-10"] = orig
        else:
            coremods["A-10"] = {"A-10C"}
    if(a10c2):
        #"A-10" : {"A-10C", "A-10A", "A-10CII"}
        if "A-10" in coremods:
            orig = coremods.get("A-10")
            orig.add("A-10CII")
            coremods["A-10"] = orig
        else:
            coremods["A-10"] = {"A-10CII"}
    if(av8b):
        coremods["AV8BNA"] = {"AV8BNA"}
    if(ajs37):
        coremods["AJS37"] = {"AJS37"}
    #WWII
    if(bf109):
        bazar["Bf-109K-4"] = ""
    if(fw190a):
        bazar["FW-190A8"] = ""
    if(fw190d):
        bazar["FW-190D9"] = ""
    if(p51):
        bazar["P-51D"] = ""
    if(p47):
        wwii["P-47D-30"] = {"P-47D-30"}
    if(spitfire):
        wwii["SpitfireLFMkIX"] = {"SpitfireLFMkIX", "SpitfireLFMkIXCW"}
    #Korea
    if(f86):
        coremods["F-86"] = {"f-86f sabre"}
        #"F-86" : {"f-86f sabre"}
    if(mig15):
        coremods["MiG-15bis"] = {"MiG-15bis"}
        #"MiG-15bis" : {"MiG-15bis"}
    #Trainer
    if(l39):
        coremods["L-39"] = {"L-39C", "L-39ZA"}
        #"L-39" : {"L-39C", "L-39ZA"}
    if(c101):
        coremods["C-101"] = {"C-101CC", "C-101EB"}
    #Modern/Fighter
    if(f18):
        zip["FA-18C"] = {"FA-18C_hornet"}
        #"FA-18C" : {"FA-18C_hornet"}
    if(f16):
        zip["F-16C"] = {"F-16C_50"}
    if(f14):
        coremods["F14"] = {"F-14A-135-GR", "f-14b"}
    if(jf17):
        coremods["ChinaAssetPack"] = {"JF-17"}
    if(m2000):
        coremods["M-2000C"] = {"M-2000C"}
    if(mig21):
        coremods["MiG-21BIS"] = {"MiG-21Bis"}
    if(f5):
        coremods["F-5E"] = {"F-5E-3"}
        #"F-5E" : {"F-5E-3"}
    #Helicopter
    if(ah64):
        coremods["AH-64D"] = {"AH-64D_BLK_II"}
    if(mi24):
        coremods["Mi-24P"] = {"Mi-24P"}
    if(mi8):
        bazar["mi-8mt"] = ""
    if(uh1):
        bazar["uh-1h"] = ""
    if(ka50):
        bazar["ka-50"] = ""
    if(sa342):
        coremods["SA342"] = {"SA342L", "SA342M", "SA342Minigun", "SA342Mistral"}
        #"SA342" :{"SA342L", "SA342M", "SA342Minigun", "SA342Mistral"}
    #FC3
    if(a10a):
        if "A-10" in coremods:
            orig = coremods.get("A-10")
            orig.add("A-10A")
            coremods["A-10"] = orig
        else:
            coremods["A-10"] = {"A-10A"}
    if(f15):
        bazar["F-15C"] = ""
    if(su25):
        bazar["su-25"] = ""
    if(su25t):
        bazar["su-25t"] = ""
    if(su27):
        bazar["su-27"] = ""
    if(su33):
        bazar["su-33"] = ""
    if(mig29):
        bazar["mig-29a"] = ""
        bazar["mig-29s"] = ""
        bazar["mig-29g"] = ""

    retlist = [coremods, bazar, wwii, zip]
    return retlist

def clear_countries(path):
    skins = os.listdir(path)
    print("Changing in " + path)
    for skin in skins:
        folder_path = path + skin
        full_path = path + skin + "\\description.lua"
        if(os.path.isdir(folder_path)):
            full_path = path + skin + "\\description.lua"
            if(sys.version_info[0] < 3):
                with open(full_path, "r") as f:
                    rows = f.readlines()
                string = cleaner(rows)
                description = open(full_path, "w")
                description.write(string)
                description.close()

            else:
                with open(full_path, "r", encoding="utf-8") as f:
                    rows = f.readlines()
                string = cleaner(rows)
                description = open(full_path, "w", encoding="utf-8")
                description.write(string)
                description.close()
        elif(os.path.isfile(folder_path)):
            extension = folder_path[-3:]
            folder_name = folder_path[:-4]
                
            if(extension == "zip"):  
                string = ""
                has_desc = False
                with zip.ZipFile(folder_path, mode="r") as infolder, zip.ZipFile(folder_name + "_new.zip", mode="w") as outfolder:
                    try:
                        infolder.getinfo("description.lua")
                        has_desc = True
                    except KeyError:
                        print(folder_path + " Does not contain description.lua")
                    if(has_desc):
                        for file in infolder.infolist():
                            if(file.filename == "description.lua"):  
                                with infolder.open("description.lua", mode="r") as desc:
                                    whole_file = desc.read().decode("utf-8")
                                    rows = whole_file.split("\n")
                                    string = cleaner(rows)
                                    outfolder.writestr("description.lua", string.encode("utf-8"), compress_type=zip.ZIP_DEFLATED)
                                desc.close()
                            else:
                                with infolder.open(file.filename, mode="r") as cont:
                                    content = cont.read()
                                    outfolder.writestr(file.filename, content, compress_type=zip.ZIP_DEFLATED)
                                cont.close()

                infolder.close()
                outfolder.close()
                os.remove(folder_path)
                temp_name = folder_name + "_new.zip"
                os.rename(temp_name, folder_path)
                print(folder_name + " is done")
                
                
                    
                    
    print("Done in " + path)

def cleaner(rows):
    string = ""
    still_countries = False
    for row in rows:
        if(still_countries):
            if("}" in row):
                string = string + "countries = {}\n"
                still_countries = False
        elif("countries =" in row or "countries=" in row):
            if("}" in row):
                string = string + "countries = {}\n"
            else:
                still_countries = True
        else:
            string = string + row
    return(string)

if __name__ == "__main__":
    main()
