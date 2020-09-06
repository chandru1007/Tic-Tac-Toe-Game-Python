import random
select_player = random.randint(1,2)
matrix=[['-' for i in range(3)] for j in range(3)]
Player1="-"
Player2="-"

def restart_matrix():
    matrix[0][0] = "-"
    matrix[0][1] = "-"
    matrix[0][2] = "-"
    matrix[1][0] = "-"
    matrix[1][1] = "-"
    matrix[1][2] = "-"
    matrix[2][0] = "-"
    matrix[2][1] = "-"
    matrix[2][2] = "-"

def display():
    print()
    print("  |  "+matrix[0][0] + "  |  "+matrix[0][1] + "  |  "+matrix[0][2] + "  |  ")
    print("  |  "+matrix[1][0] + "  |  "+matrix[1][1] + "  |  "+matrix[1][2] + "  |  ")
    print("  |  "+matrix[2][0] + "  |  "+matrix[2][1] + "  |  "+matrix[2][2] + "  |  ")
    print()

def check_game(Player_):
    if   matrix[0][0] == Player_ and matrix [0][1] == Player_ and matrix[0][2] == Player_:
        return 1
    elif matrix[1][0] == Player_ and matrix [1][1] == Player_ and matrix[1][2] == Player_:
        return 1
    elif matrix[2][0] == Player_ and matrix [2][1] == Player_ and matrix[2][2] == Player_:
        return 1
    elif matrix[0][0] == Player_ and matrix [1][0] == Player_ and matrix[2][0] == Player_:
        return 1
    elif matrix[0][1] == Player_ and matrix [1][1] == Player_ and matrix[2][1] == Player_:
        return 1
    elif matrix[0][2] == Player_ and matrix [1][2] == Player_ and matrix[2][2] == Player_:
        return 1
    elif matrix[0][0] == Player_ and matrix [1][1] == Player_ and matrix[2][2] == Player_:
        return 1
    elif matrix[0][2] == Player_ and matrix [1][1] == Player_ and matrix[2][0] == Player_:
        return 1
    else:
        return 0

def self_lost(select_player,flag):
    print("------------------------------------------------------------")
    print()
    if flag==0:
        print("Sorry! The place is already filled. YOU LOST THE GAME!...")
    elif flag==1:
        print("Sorry! You Entered a wrong number. YOU LOST THE GAME!...")
    print()

    if select_player == 1 and (flag == 1 or flag == 0):
        print("Player {} Wins :)".format(select_player + 1))
    elif select_player == 2 and (flag == 1 or flag == 0):
        print("Player {} Wins :)".format(select_player - 1))
    print()
    print("--------------------------GAME OVER--------------------------")
    return 0

def draw():
    print("-------------------------------------------------------------")
    print("                        DRAW MATCH                           ")
    print("--------------------------GAME OVER--------------------------")
    print()
    print("----------Final board----------")
    display()

def set_matrix(input_,Player_,select_player):
    flag =0
    if   input_ == 1   and   matrix[0][0] == "-":
        matrix[0][0]=Player_
        flag=1
    elif input_ == 2   and   matrix[0][1] == "-":
        matrix[0][1]=Player_
        flag=1
    elif input_ == 3   and   matrix[0][2] == "-":
        matrix[0][2]=Player_
        flag=1
    elif input_ == 4   and   matrix[1][0] == "-":
        matrix[1][0]=Player_
        flag=1
    elif input_ == 5   and   matrix[1][1] == "-":
        matrix[1][1]=Player_
        flag=1
    elif input_ == 6   and   matrix[1][2] == "-":
        matrix[1][2]=Player_
        flag=1
    elif input_ == 7   and   matrix[2][0] == "-":
        matrix[2][0]=Player_
        flag=1
    elif input_ == 8   and   matrix[2][1] == "-":
        matrix[2][1]=Player_
        flag=1
    elif input_ == 9   and   matrix[2][2] == "-":
        matrix[2][2]=Player_
        flag=1
        
    if flag == 0:
        if self_lost(select_player,flag) == 0:
            return 0
    else:
        if check_game(Player_):
            print()
            print("------------------------------------------------------------")
            if select_player == 1:
                print("Player {} Wins :)".format(select_player))
            elif select_player == 2:
                print("Player {} Wins :)".format(select_player))
            else:
                print("Player {} Wins :)".format(select_player-1))

            print("--------------------------GAME OVER--------------------------")
            print()
            print("----------Final board----------")
            display()
            print("--------------------------------")
            return 0
        else:
            display()
            return 1

def main_content(game):
    while game:
        x,o="X","O"
        print("Player {} Starts the Game Choose {} or {}".format(select_player,x,o))
        select_x_o=input().upper()
        if select_x_o == "X" or select_x_o == "O":
            if select_player == 1:
                if select_x_o == "X":
                    Player1="X"
                    Player2="O"
                elif select_x_o == "O":
                    Player1="O"
                    Player2="X"
            elif select_player == 2:
                if select_x_o == "X":
                    Player2="X"
                    Player1="O"
                elif select_x_o == "O":
                    Player2="O"
                    Player1="X"
            
            print("Player 1 = {} ".format(Player1))
            print("Player 2 = {} ".format(Player2))
            print()
            game_over=0
            if select_player == 1:
                for i in range(1,10):
                    if game_over == 0:
                        if i%2 !=0:
                            print("Player {} Enter between [1-9](both inclusive)]".format(select_player))
                            input1=int(input())
                            if input1 >= 1 and input1 <= 9:
                                if set_matrix(input1,Player1,select_player) == 0:
                                    game_over = 1
                                else:
                                    game_over = 0
                            else:
                                if self_lost(select_player,1) == 0:
                                    game_over = 1
                                else:
                                    game_over = 0
                        else:
                            print("Player {} Enter between [1-9](both inclusive)]".format(select_player+1))
                            input1=int(input())
                            if input1 >= 1 and input1 <= 9:
                                if set_matrix(input1,Player2,select_player+1) == 0:
                                    game_over = 1
                                else:
                                    game_over = 0
                            else:
                                if self_lost(select_player+1,1) == 0:
                                    game_over = 1
                                else:
                                    game_over = 0
                if game_over == 0:
                    draw()
                    
            else:
                for i in range(0,9):
                    if game_over == 0:
                        if i%2 ==0:
                            print("Player {} Enter between [1-9](both inclusive)]".format(select_player))
                            input1=int(input())
                            if input1 >= 1 and input1 <= 9:
                                if set_matrix(input1,Player2,select_player) == 0:
                                    game_over = 1
                                else:
                                    game_over = 0
                            else:
                                if self_lost(select_player,1) == 0:
                                    game_over = 1
                                else:
                                    game_over = 0
                        else:
                            print("Player {} Enter between [1-9](both inclusive)]".format(select_player-1))
                            input1=int(input())
                            if input1 >= 1 and input1 <= 9:
                                if set_matrix(input1,Player1,select_player-1) == 0:
                                    game_over = 1
                                else:
                                    game_over = 0
                            else:
                                if self_lost(select_player-1,1) == 0:
                                    game_over = 1
                                else:
                                    game_over = 0
                if game_over == 0:
                    draw()
        else:
            print()
            print("---------------------------------------")
            print("           Wrong input                 ")
            print("********** Game Over ******************")
            print("---------------------------------------")
            print()
        print("Do you want to restart the game (YES/NO)")
        restart=input().upper()
        if restart == "YES":
            restart_matrix()
            print("----------Current board----------")
            display()
            print("---------------------------------")
            game=True
        elif restart == "NO":
            game=False
    print("---------------------------------------")
    print("             Thank You                 ")
    print("---------------------------------------")
        
if __name__ == "__main__":
    print()
    print("----------Current board----------")
    display()
    print("---------------------------------")
    print()
    main_content(game=True)
    
