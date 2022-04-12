print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

field = list(range(1, 10))
def main(field):
    counter = 0
    win = False
    while not win:
        game_field(field)
        if counter % 2 == 0:
           data_input("X")
        else:
           data_input("O")
        counter += 1
        if counter > 4:
           vic = combinations_win(field)
           if vic:
              print(vic, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break



def game_field(field):
   print("-" * 13)
   for i in range(3):
      print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
      print("-" * 13)


def data_input(player_number):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_number + "?")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(field[player_answer-1]) not in "XO"):
            field[player_answer-1] = player_number
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def combinations_win(field):
   win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
   for each in win_coord:
       if field[each[0]] == field[each[1]] == field[each[2]]:
          return field[each[0]]
   return False

main(field)

input("Нажмите Enter для выхода!")



