#This is one of my first programs in python. It is a simple tic tac toe game with the design hardcoded.
#It will create a board and it will alternate between two players taking turns until one of the win
#   or they tie.
#Esteban Sierra
#05/20/17


#Future improvements:
#-Being able to play against a computer


# Creating a row
def format_row(row):
  return  '|'.join('{0:^3}'.format(x) for x in row)

#Creating the board
def format_board(board):
  # for a single list with 9 elements uncomment the following line:
  return '\n\n'.join(format_row(row) for row in zip(*[iter(board) ] *3))
  # for a 3x3 list:
  # return '\n\n'.join(format_row(row) for row in board)

#Check if a player has won by going through patterns
def check_4win(player):
  if board[0] == board[1] == board[2]==player:
    print( player+' won')
    return True
  if board[3] == board[4] == board[5]==player:
    print( player+' won')
    return True
  if board[6] == board[7] == board[8]==player:
    print( player+' won')
    return True
  if board[0] == board[3] == board[6]==player:
    print( player+' won')
    return True
  if board[1] == board[4] == board[7]==player:
    print( player+' won')
    return True
  if board[2] == board[5] == board[8]==player:
    print( player+' won')
    return True
  if board[0] == board[4] == board[8]==player:
    print( player+' won')
    return True
  if board[2] == board[4] == board[6]==player:
    print( player+' won')
    return True

#Clean the baord
def clean_board(board):
  for cell in board:
    cell = ' '
  return board

list = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
turn = 1
won = False

print('\t--Welcome to Tic Tac Toe--')
print ('--------------------------------')
print('Instructions:')
print ('--------------------------------')
print('Pick between 1-9 depending where you want to mark.')
print('')
print(format_board(list))
print ('--------------------------------')
print('\tGame Start')
print ('--------------------------------')
empty_board = [' ' ,' ' ,' ' ,' ' ,' ' ,' ' ,' ' ,' ' ,' ']
board = [' ' ,' ' ,' ' ,' ' ,' ' ,' ' ,' ',' ' ,' ']
player1 = 'X'
player2 = 'O'

#Main while loop that runs the game in here
#For Python 2.7 use raw_input instead of input)
while not won:
  print('Player 1\tPlayer 2')
  #This will keep taking turns with players
  if(turn%2 !=0 ):

    print('********')
    print(format_board(board))
    cell_selected = int(input('Your pick: '))
    if board[cell_selected-1] == ' ':
      board[cell_selected-1] = player1
    won = check_4win(player1)
  else:
    print('\t\t\t********')
    print(format_board(board))
    cell_selected = int(input('Which cell you want to mark?'))
    if board[cell_selected-1] == ' ':
      board[cell_selected-1] = player2
    won = check_4win(player2)
  if won:
    print (format_board(board))
    play_again = input('Do you wish to play again? (y/n)')
    if play_again == 'y':
      won = False
      board = empty_board
  turn +=1

