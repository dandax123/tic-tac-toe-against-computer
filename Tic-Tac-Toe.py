# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:06:22 2019

@author: OLUKARE DANIEL
"""

import random
TURN=0
WIN=False
Num_Moves=0
turnchecker=False
turnchooser=random.randint(0,1)
if turnchooser<=0.5:
    TURN=0
else:
    TURN=1
def freespot(Board):
    freerow=0
    freecol=0
    if(Num_Moves==8):
        for i in range(0,3):
            for j in range(0,3):
                if(Board[i][j]=="-"):
                    freerow=i
                    freecol=j
    return freerow, freecol
def Check_WINNER(Board):
    # Check Rows
    for i in range(3):
        if Board[i][0]!='-' and Board[i][0]==Board[i][1] and Board[i][1]==Board[i][2]:
            return(True)
    # Check Columns
    for i in range(3):
        if Board[0][i]!='-' and Board[0][i]==Board[1][i] and Board[1][i]==Board[2][i]:
            return(True)
    # Check Diagonal
    if Board[0][0]!='-' and Board[0][0]==Board[1][1] and Board[1][1]==Board[2][2]:
        return(True)
    if Board[0][2]!='-' and Board[0][2]==Board[1][1] and Board[1][1]==Board[2][0]:
        return(True)    
    
    return(False)
    
def printBoard(Board):
    for i in range(3):
        for j in range(3):
            print(Board[i][j], end=" ")
        print()

Board=[["-","-","-"],["-","-","-"],["-","-","-"]]
def choosepossiblewin(Board):
    rowin=0
    cowin=0
    if(Board[0][0]==Board[1][1] and TURN!=0 and Board[1][1]=="O"):
        if(Board[2][2]=="-"):
            rowin=2
            cowin=2
    elif(Board[0][0]==Board[2][2] and TURN!=0 and Board[0][0]=="O"):
       if(Board[1][1]=="-"):
            rowin=1
            cowin=1
    elif(Board[2][2]==Board[1][1] and TURN!=0 and Board[1][1]=="O"):
        if(Board[0][0]=="-"):
            rowin=0
            cowin=0
    elif(Board[0][0]==Board[0][1] and TURN!=0 and Board[0][1]=="O"):
       if(Board[0][2]=="-"):
            rowin=0
            cowin=2
    elif(Board[0][2]==Board[0][1] and TURN!=0 and Board[0][1]=="O"):
        if(Board[0][0]=="-"):
            rowin=0
            cowin=0
    elif(Board[0][0]==Board[0][2] and TURN!=0 and Board[0][2]=="0"):
        if(Board[0][2]=="-"):
            rowin=0
            cowin=1
    
    elif(Board[1][0]==Board[1][1] and TURN!=0 and Board[1][1]=="O"):
       if(Board[1][2]=="-"):
            rowin=1
            cowin=2
    elif(Board[1][2]==Board[1][1] and TURN!=0 and Board[1][1]=="O"):
        if(Board[1][0]=="-"):
            rowin=1
            cowin=0
    elif(Board[1][0]==Board[1][2] and TURN!=0 and Board[1][2]=="O"):
        if(Board[1][2]=="-"):
            rowin=1
            cowin=1
    

    elif(Board[2][0]==Board[2][1] and TURN!=0 and Board[2][1]=="O"):
       if(Board[2][2]=="-"):
            rowin=2
            cowin=2
    elif(Board[2][2]==Board[2][1] and TURN!=0 and Board[2][1]=="O"):
        if(Board[2][0]=="-"):
            rowin=2
            cowin=0
    elif(Board[2][0]==Board[2][2] and TURN!=0 and Board[2][2]=="O"):
        if(Board[2][2]=="-"):
            rowin=2
            cowin=1
    
    
    elif(Board[0][0]==Board[1][0] and TURN!=0 and Board[1][0]=="O"):
       if(Board[2][0]=="-"):
            rowin=2
            cowin=0
    elif(Board[2][0]==Board[1][0] and TURN!=0 and Board[1][0]=="O"):
        if(Board[0][0]=="-"):
            rowin=0
            cowin=0
    elif(Board[0][0]==Board[2][0] and TURN!=0 and Board[2][0]=="O"):
        if(Board[1][0]=="-"):
            rowin=1
            cowin=0
    
    elif(Board[0][1]==Board[1][1] and TURN!=0 and Board[1][1]=="O"):
       if(Board[2][1]=="-"):
            rowin=2
            cowin=1
    elif(Board[2][1]==Board[1][1] and TURN!=0 and Board[1][1]=="O"):
        if(Board[0][1]=="-"):
            rowin=0
            cowin=1
    elif(Board[0][1]==Board[2][1] and TURN!=0 and Board[2][1]=="O"):
        if(Board[1][1]=="-"):
            rowin=1
            cowin=1
    
    elif(Board[0][2]==Board[1][2] and TURN!=0 and Board[1][2]=="O"):
       if(Board[2][2]=="-"):
            rowin=2
            cowin=2
    elif(Board[2][2]==Board[1][2] and TURN!=0 and Board[1][2]=="O"):
        if(Board[0][2]=="-"):
            rowin=0
            cowin=2
    elif(Board[0][2]==Board[2][2] and TURN!=0 and Board[2][2]=="O"):
        if(Board[1][2]=="-"):
            rowin=1
            cowin=2
    elif(Board[0][2]==Board[1][1] and TURN!=0 and Board[1][1]=="O"):
        if(Board[2][0]=="-"):
            rowin=2
            cowin=0
    elif(Board[2][0]==Board[1][1] and TURN!=0 and Board[1][1]=="O"):
        if(Board[0][2]=="-"):
            rowin=0
            cowin=2
    elif(Board[0][2]==Board[2][0] and TURN!=0 and Board[2][0]=="O"):
        if(Board[1][1]=="-"):
            rowin=1
            cowin=1
    
    return rowin,cowin
    
    
def rowcheck(Board):
    rowe=-1
    cole=-1
    # first row
    if(Board[0][0]==Board[0][1] and Board[0][1]!="-" and Board[0][1]!='O'):
        rowe=0
        cole=2
        if(Board[0][2]=="O"):
            rowe=-1
            cole=-1
    elif(Board[0][0]==Board[0][2] and Board[0][0]!="-" and Board[0][0]!='O'):
        rowe=0
        cole=1
        if(Board[0][1]=="O"):
            rowe=-1
            cole=-1
    elif(Board[0][2]==Board[0][1] and Board[0][1]!="-" and Board[0][1]!='O'):
        rowe=0
        cole=0
        if(Board[0][0]=="O"):
            rowe=-1
            cole=-1
    #second row
    elif(Board[1][0]==Board[1][1] and Board[1][1]!="-" and Board[1][0]!='O'):
        rowe=1
        cole=2
        if(Board[1][2]=="O"):
            rowe=-1
            cole=-1
    elif(Board[1][0]==Board[1][2] and Board[1][0]!="-" and Board[1][0]!='O'):
        rowe=1
        cole=1
        if(Board[1][1]=="O"):
            rowe=-1
            cole=-1
    elif(Board[1][2]==Board[1][1] and Board[1][1]!="-" and Board[1][1]!='O'):
        rowe=1
        cole=0
        if(Board[1][0]=="O"):
            rowe=-1
            cole=-1
    #third row
    elif(Board[2][0]==Board[2][1] and Board[2][1]!="-" and Board[2][0]!='O'):
        rowe=2
        cole=2
        if(Board[2][2]=="O"):
            rowe=-1
            cole=-1
    elif(Board[2][0]==Board[2][2] and Board[2][0]!="-" and Board[2][2]!='O'):
        rowe=2
        cole=1
        if(Board[2][1]=="O"):
            rowe=-1
            cole=-1
    elif(Board[2][2]==Board[2][1] and Board[2][1]!="-" and Board[2][1]!='O'):
        rowe=2
        cole=0
        if(Board[2][0]=="O"):
            rowe=-1
            cole=-1
    return rowe,cole      
def Columncheck(Board):
    row=-1
    col=-1
    if(Board[0][0]==Board[1][0] and Board[1][0]!="-" and Board[1][0]!='O'):
        row=2
        col=0
        if(Board[2][0]=="O"):
            row=-1
            col=-1
    elif(Board[0][0]==Board[2][0] and Board[0][0]!="-" and Board[2][0]!='O'):
        row=1
        col=0
        if(Board[1][0]=="O"):
            row=-1
            col=-1
    elif(Board[2][0]==Board[1][0] and Board[1][0]!="-" and Board[1][0]!='O'):
        row=0
        col=0
        if(Board[0][0]=="O"):
            row=-1
            col=-1

    #second row
    elif(Board[0][1]==Board[1][1] and Board[1][1]!="-" and Board[1][1]!='O'):
        row=2
        col=1
        if(Board[2][1]=="O"):
            row=-1
            col=-1

    elif(Board[0][1]==Board[2][1] and Board[0][1]!="-" and Board[0][1]!='O'):
        row=1
        col=1
        if(Board[1][1]=="O"):
            row=-1
            col=-1

    elif(Board[2][1]==Board[1][1] and Board[1][1]!="-" and Board[1][1]!='O'):
        row=0
        col=1
        if(Board[0][1]=="O"):
            row=-1
            col=-1

    #third row
    elif(Board[0][2]==Board[1][2] and Board[1][2]!="-" and Board[1][2]!='O'):
        row=2
        col=2
        if(Board[2][2]=="O"):
            row=-1
            col=-1

    elif(Board[0][2]==Board[2][2] and Board[0][2]!="-" and Board[0][2]!='O'):
        row=1
        col=2
        if(Board[1][2]=="O"):
            row=-1
            col=-1

    elif(Board[2][2]==Board[1][2] and Board[1][2]!="-" and Board[1][2]!='O'):
        row=0
        col=2
        if(Board[0][2]=="O"):
            row=-1
            col=-1

    return row,col     
    # Check Diagonal
def leftdiagonalcheck(Board):
    randrowe=-1
    randcole=-1
    if Board[0][0]!='-' and Board[0][0]==Board[1][1] and Board[1][1]!='O':
        randrowe=2
        randcole=2
        if(Board[2][2]=="O"):
            randrowe=-1
            randcole=-1

    elif Board[1][1]==Board[2][2] and Board[1][1]!="-" and Board[1][1]!='O':
        randrowe=0
        randcole=0
        if(Board[0][0]=="O"):
            randrowe=-1
            randcole=-1

    elif Board[2][2]==Board[0][0] and Board[2][2]!="-" and Board[2][2]!='O':
        randrowe=1
        randcole=1
        if(Board[1][1]=="O"):
            randrowe=-1
            randcole=-1

    else:
        randrowe=-1
        randcole=-1
    return randrowe,randcole
def rightdiagonalcheck(Board):
    randrow=-1
    randcol=-1
    if Board[0][2]!='-' and Board[0][2]==Board[1][1] and Board[1][1]!='O':
        randrow=2
        randcol=0
        if(Board[2][0]=="O"):
            randrow=-1
            randcol=-1
            
    elif Board[1][1]==Board[2][0] and Board[2][0]!="-" and Board[2][0]!='O':
        randrow=0
        randcol=2
        if(Board[0][2]=="O"):
            randrow=-1
            randcol=-1

    elif Board[0][2]==Board[2][0] and Board[0][2]!="-" and Board[0][2]!='O':
        randrow=1
        randcol=1
        if(Board[1][1]=="O"):
            randrow=-1
            randcol=-1
    else:
        randrow=-1
        randcol=-1  
        
    return randrow,randcol  
def chooser(Board):
    rha,a=rowcheck(Board)
    cha,b=Columncheck(Board)
    ldc,c=leftdiagonalcheck(Board)
    rdc,d=rightdiagonalcheck(Board)
    rowchoice=random.randint(0,2)
    colchoice=random.randint(0,2)
    #print("rha",rha,a)
    #print("cha",cha,b)
    #print("ldc",ldc,c)
    #print("rdc",rdc,d)
    if(Num_Moves>=2):
        if(rha>=0 and (cha<0) and (ldc<0) and (rdc<0)):
            rha,a=rowcheck(Board)
            return rha,a
        elif(cha>=0 and (rha<0) and (ldc<0) and (rdc<0)):
            #print("cha",cha,b)
            cha,b=Columncheck(Board)
            return cha,b
        elif(ldc>=0 and (rha<0) and (cha<0) and (rdc<0)):
            #print("ldc",ldc,c)
            ldc,c=leftdiagonalcheck(Board)
            return ldc,c
        elif(rdc>=0 and (rha<0) and (cha<0) and (ldc<0)):
            rdc,d=rightdiagonalcheck(Board)
            #print("rdc",rdc,d)
            return rdc,d
        elif(rha>=0 and cha>=0 and(ldc<0) and (rdc<0)):
            return rha,a
        elif(cha>=0 and rdc>=0 and(rha<0) and (ldc<0)):
            return cha,b
        elif(cha>=0 and ldc>=0 and(rha<0) and (rdc<0)):
            return ldc,c
        elif(rha>=0 and rdc>=0 and(cha<0) and (ldc<0)):
            return rdc,d
        elif(rha>=0 and ldc>=0 and(cha<0) and (rdc<0)):
            return ldc,c
        else:
            specialrow,specialcol=choosepossiblewin(Board)
            return specialrow, specialcol
    elif( not WIN and Num_Moves==8):
        x,y=freespot(Board)
        return x,y
    elif(Num_Moves<3):
        #return rowchoice,colchoice
        #("random",rowchoice,colchoice)
        return rowchoice,colchoice


printBoard(Board)
while (not WIN) and Num_Moves <= 8:
    if TURN==0:
        print("This is PLAYER X'S Turn:")
        Check_Move=False
        while not Check_Move:
            Row,Col=[int(x) for x in input("Enter the row and column of your tile (SPACE SEPARATED): ").split(" ")]
            if Board[Row-1][Col-1]!='-':
                print("That position if already played. Enter the new tile position")
            else:
                Check_Move=True
            
        Board[Row-1][Col-1]='X'
        printBoard(Board)
        TURN=1
        Num_Moves += 1
        if Num_Moves > 4:
            WIN=Check_WINNER(Board)
        if WIN:
            print("CONGRATULATIONS PLAYER X:")
            print("YOU ARE THE WINNER")
    else:
        print("This is PLAYER O'S Turn:")
        Check_Move=False
        while not Check_Move:
            Row,Col=chooser(Board)
            print("chooser value",Row, Col)
            if Board[Row][Col]!='-':
                print("That position if already played. Generating another position")
            else:
                Check_Move=True
                
        Board[Row][Col]='O'
        printBoard(Board)
        TURN=0
        Num_Moves += 1
        if Num_Moves > 4:
            WIN=Check_WINNER(Board)
        if WIN:
            print("CONGRATULATIONS PLAYER O:")
            print("YOU ARE THE WINNER")
if not WIN:
    print("The Game ended as a tie")