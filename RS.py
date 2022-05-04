import random

Restaurant_Daily_Income = 0

Menu = [
    ["Burger", 4.51],
    ["Steak", 4.21],
    ["Sushi", 3.31],
    ["Fries", 1.21],
    ["Vanilla Shake", 4.50],
    ["Beer", 5.00]
]

def Tab_Gen():
    Tab = []
    for i in range(random.randrange(2, 8)):
        Tab.append(Menu[random.randrange(1, 6)])
    return Tab

def CheckOut():
    global Restaurant_Daily_Income
    Price = 0
    Final_Tab = Tab_Gen()
    Final_Tab_Formatted_For_Print = "".join(map(str, [Price for Price in Final_Tab])).replace("[", "").replace("]", "\n")
    for Item in range(len(Final_Tab)):
        Price += Final_Tab[Item][1]
        
    Restaurant_Daily_Income += Price

    return [round(Price, 2), Final_Tab_Formatted_For_Print]

for i in range(random.randrange(4, 8)):
    Check_Out_Info = CheckOut()
    print()
    print(Check_Out_Info[1])
    print("Check Out Amount: ", Check_Out_Info[0])
    print("Daily Income", round(Restaurant_Daily_Income, 2))