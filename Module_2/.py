# lijst1 =    ['codewars', 'flick', 'code', 'wars']
# lijst2 =    ['flick', 'chocolate', 'adventure', 'sunshine'] 
# lijst3 =   ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] 


# def flick_switch(lijst3):
#     fout = False
#     goed = True

#     for x in range(len(lijst3)):    
#         if lijst3[x] == "flick":
#             goed, fout = fout, goed
#             lijst3[x] = goed
            
#         else:
#             lijst3[x] = goed

#     return lijst3
    

# flick_switch(lijst3)
# print(lijst3)


("------------------------------------------------")

# namen_lijst = []
# lootjes_trekken = False

# while not lootjes_trekken:
#     naam = input("Voer een naam in: ")
#     while True:
#         if naam in namen_lijst:
#             print("Voer een nieuwe naam in")
#         else:
#             namen_lijst.append(naam)
#             break

#     if len(namen_lijst) >= 3:
#         lootjes_trekken = input("wilt u de lootjes trekken (j/n)") == 'j'

# for naam in namen_lijst:
#     print(naam)

("------------------------------------------------")

# def score(dice):
#     score = 0
#     if dice.count(4) >= 3:
#         score += 400
            
#     if dice.count(1) >= 3:
#         score += 1000
#         score -= 300
        
#     for x in dice:
#         if x == 1:
#             score += 100
    
#         if x == 5:
#             score += 50
        
#     return score


