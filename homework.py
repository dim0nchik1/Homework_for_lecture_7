balans_list = ['(((([{}]))))'
               '[([])((([[[]]])))]'
               '{()}{{[()]}}']


unbalanced_sequences = ['}{}'
                        '{{[(])]}}'
                        '[[{())}]']


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) != 0:
            return True
        return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack == 0:
            return None
        item = self.stack.pop()
        return item

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]


    def size(self):

        return len(self.stack)

    def check_ballance(string):
        stack_list = []
        for item in string:
            if item in '{([':
                stack_list.append(item)

            elif item in '})]':
                if not stack_list:
                    return 'Несбалансированно'
                if item == ')' and stack_list[-1] == '(':
                    stack_list.pop()
                elif item == '}' and stack_list[-1] == '{':
                    stack_list.pop()
                elif item == ']' and stack_list[-1] == '[':
                    stack_list.pop()
                else:
                    return 'Несбалансировано'
        if not stack_list:
            return 'Сбалансировано'
        else:
            return 'Несбалансировано'




if __name__ == '__main__':
    for string in balans_list:
        print(Stack.check_ballance(string))
    for string in unbalanced_sequences:
        print(Stack.check_ballance(string))


