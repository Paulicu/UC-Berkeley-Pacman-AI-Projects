class CalculatorException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Calculator(object):
    def read(self) :
        '''read input from stdin'''
        return input('> ')
    
    def eval(self, string) :
        '''evaluates an infix arithmetic expression '''
        #TODO implement me
        pass

    def loop(self) :
        """read a line of input, evaluate and print it
        repeat the above until the user types 'quit'. """
        line = self.read()
        #TODO implement me
        pass

if __name__ == '__main__':
    calc = Calculator()
    calc.loop()