#!/usr/bin/env python
# coding: utf-8

# In[1]:


board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
available=9
turn='Player1'
value='X'

def display_board():
    global turn
    print('\n')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')
    print(f'-------------')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print(f'-------------')
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print('\n'+turn.upper()+' chance')
        


# In[2]:


def choice():
    while True:
        choice=input('Select number from (1-9)')
        if(choice.isdigit() == False or int(choice)<=0) or (int(choice) not in range(1,10)):
            print('Invalid choice')
            continue;
        else : 
            break
        
    return int(choice)
    


# In[3]:


def check_winner():
    global board
    
    if(board[6]==board[7]==board[8]!=' ' or 
       board[3]==board[4]==board[5]!=' ' or
       board[0]==board[1]==board[2]!=' ' or 
       board[6]==board[3]==board[0]!=' ' or
       board[7]==board[4]==board[1]!=' ' or
       board[8]==board[5]==board[2]!=' ' or
       board[6]==board[4]==board[2]!=' ' or
       board[0]==board[4]==board[8]!=' ' ):
        return True
    else:
        return False


# In[4]:


def update_board(choice):
    global turn
    global value
    global available
    
    if(board[choice]==' '):
        board[choice]=value
        available = available -1
        if value=='X':
                value='O'
        else:
                value='X'
            
        if turn=='Player1':
                turn='Player2'
        else:
                turn='Player1'
    else:
        print('That block is occupied')


# In[5]:


def start_game():
    play=True
    global turn
    global value
    global available
    global board
    
    while play==True:
        display_board()
        chance = input(turn + " Choose 'X' or 'O'\n")
        print('\n')
        if(chance == 'X'or chance=='x' ):
            turn='Player1'
        else:
            turn='Player2'
            
        print(turn+' => X')
        
        if(turn == 'Player1'):
            print('Player2 => O')
        else:
            print('Player1 => O')


        
        while available!=0:
            display_board()
            userchoice=choice()-1
            update_board(userchoice)
            if check_winner():
                if turn=='Player1':
                    turn='Player2'
                else:
                    turn='Player1'
                display_board()
                print('Congratulations '+turn+' won this game!')
                break

        
        

        
        
        stillplay=input('Do you want to Play TIC-TAC-TOE? (Y/N)')
        board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        turn='Player1'
        value='X'
        available=9
        play = (stillplay=='Y')
        
    


# In[6]:


start_game()


# In[ ]:




