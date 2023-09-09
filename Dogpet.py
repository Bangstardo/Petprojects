class Dog:
    def __init__(self, name, bark):
        self.name = name
        self.bark = bark

    def pet(self):
        print(f'{self.name} appears to be be happy, {self.bark} he goes!')
        try:
            with open('pidigitsog.txt') as f:
                f.read()

        except FileNotFoundError:
            print(f'{self.bark} you have no file {self.bark}')
        else:
            print(f'{self.name} is a good boy *{self.bark}*')
        finally:
            print(f'{self.name} thinks the planet is collapsing')


dawg = Dog('snoop', 'Woof, Woof D O DOUBLE G')

dawg.pet()
