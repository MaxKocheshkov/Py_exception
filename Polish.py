# Task 1
def polish(lst):
  user_input = []
  operation = {
            '+': lambda x,y: x.__add__(y),
            '-': lambda x,y: x.__sub__(y),
            '*': lambda x,y: x.__mul__(y),
            '/': lambda x,y: x.__truediv__(y)
        }
  for user_index in lst:
    if user_index[0] == operation.keys():
      user_input.append(int(user_index[0]))
      continue
    else:
      assert user_index[0] in operation.keys(), 'Это никогда не должно произойти'
    try:
        y = lst.pop()
        x = lst.pop()
        if int(x) >= 0 and int(y) >= 0:
          z = operation[user_index[0]](int(x), int(y))
          user_input.append(z)
        else:
          print('Вводимые значения должны быть больше нуля!')
          return
    except (KeyError, IndexError, ValueError):
      print('Проверьте вводимые значения')
    except ZeroDivisionError:
      print('Деление на ноль!')
    else:
      return user_input.pop()

lst = input('Enter expression: ').split()
print(polish(lst))
