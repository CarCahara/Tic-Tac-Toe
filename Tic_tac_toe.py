# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:57:25 2019

@author: eedo
"""
import random
import sys

def display_board(board): #display board in plan view
    print(f"""{board[6]} | {board[7]} | {board[8]}\n---------\n{board[3]} | {board[4]} | {board[5]}\n---------\n{board[0]} | {board[1]} | {board[2]}""")

def player_input(): #Ask for marker choice
    player1 = ''
    player2 = ''
    while 'X' not in player1 + player2:
        player1 = input("Player 1 is (enter 'X' or 'O'): ").upper()
        if player1 == 'X':
            player2 = 'O'
        elif player1 == 'O':
            player2 = 'X'
    print (f'Player 1 is {player1}, player 2 is {player2}')

def place_marker(board, marker, position): #function to place marker on position
    board[position - 1] = marker

    

def win_check(board, mark): #check if someone won (to be called after each turn)
    triple = [mark] * 3
    #check horizontal
    if board[0:3] == triple or board [3:6] == triple or board[6:] == triple:
        return True
    #check vertical
    if board[0::3] == triple or board [1::3] == triple or board[2::3] == triple:
        return True
    #check diagonal
    if board[::4] == triple or board[2:7:2] == triple:
        return True
    else:
        return False

def choose_first(): #Randomly choose who goes first
    global marker
    first = random.randint(1,2)
    print(f'Player {first} goes first.')
    if first == 1:
        marker = 'X'
    else:
        marker = 'O'
        
def space_check(board, position): #Check if space on the board is free
    
    return board[position - 1] == " "

def full_board_check(board): #check if board is filled
    
    return " " not in board

def player_choice(board): #ask player for next position and call space_check function to determine if free
    
    while True:
        
        pos = int(input("Choose next position (1 - 9): "))
        
        if pos < 1 or pos > 9:
            print("Position out of range. Please choose a position between 1 - 9.")
            continue
        elif space_check(board, pos):
            return pos
        else:
            print(f"Position {pos} is not free. Please choose another positon.")
            continue
        
def replay(): #Ask to play again
    
    while True:
        again = input("Play again ('Y' or 'N')? ")
        if again.upper() == 'Y':
            return True
        elif again.upper() == 'N':
            return False

while True: #Actual game sequence
    print('Welcome to Tic Tac Toe! Positions as follows: ')
    board = [" "] * 9
    display_board([1, 2, 3, 4, 5, 6, 7, 8, 9])
    marker = ''
    player_input()
    choose_first()
    
    while not full_board_check(board):
        place_marker(board, marker, player_choice(board))
        display_board(board)
        if win_check(board, marker):
            print(f"{marker} wins!")
            if replay():
                board = [" "] * 9
                print("Loser goes first.")
                if marker == 'X':
                    marker = 'O'
                elif marker == 'O':
                    marker = 'X'
                continue
            else:
                print("Thanks for playing.")
                sys.exit()
        if marker == 'X':
            marker = 'O'
        elif marker == 'O':
            marker = 'X'
        if full_board_check(board):
            print("Tie!")
    if replay():
        continue
    else:
        print("Thanks for playing.")
        break
