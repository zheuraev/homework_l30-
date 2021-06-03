# Ввести некоторое число и записать его цифры в стек, который нужно реализовать.
# Вывести это число из стека так, чтобы его цифры шли в обратном порядке.


class Stack:
    def __init__(self, number):
        self.number = list(str(number))

    def append(self, new_numeral):
        self.number.append(new_numeral)

    def pop(self):
        self.number.pop()

    def __str__(self):
        self.number.reverse()
        return ' '.join(str(val) for val in self.number)



def main():
    stack = Stack(123)
    stack.append(4)
    stack.append(5)
    stack.append(6)
    print(stack)


if __name__ == '__main__':
    main()
