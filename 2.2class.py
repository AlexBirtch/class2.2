class Animals:
    total_weight = 0
    max_weight = 0
    max_weight_name = ''

    def __init__(self, name='Без имени', weight=1):
        self.name = name
        self.weight = weight
        Animals.total_weight += self.weight

        if self.weight > Animals.max_weight:
            Animals.max_weight = self.weight
            Animals.max_weight_name = self.name

    def feed(self):
        return f'{self.name} - покормлен(а)'

    def action(self):
        return 'погладить =)'

class Chicken(Animals):
    class_name = 'курица'

    def get_voice(self):
        return 'ko-ko'

    def action(self):
        return 'собирать яйца'

class Duck(Animals):
    class_name = 'утка'

    def get_voice(self):
        return 'кря-кря'

    def action(self):
        return 'собирать яйца'

class Guse(Animals):
    class_name = 'гусь'

    def get_voice(self):
        return 'кря-кря'

    def action(self):
        return 'собирать яйца'

class Cow(Animals):
    class_name = 'корова'

    def get_voice(self):
        return 'му-му'

    def action(self):
        return 'доить'

class Sheep(Animals):
    class_name = 'овца'

    def get_voice(self):
        return 'бе-бе'

    def action(self):
        return 'стричь'

class Goat(Animals):
    class_name = 'коза'

    def get_voice(self):
        return 'бле-бле'

    def action(self):
        return 'доить'

# гуси
guce_grey = Guse('Серый', 7)
guce_white = Guse('Белый', 5)

# куры
chicken_koko = Chicken('Ко-ко', 3)
rooster = Chicken('Кукареку', 4)

# утка
duck = Duck('Кряк-Кряква', 5)

# корова
cow = Cow('Манька', 150)

# овцы
sheep_barash = Sheep('Барашек', 45)
sheep_curly = Sheep('Кудрявый', 60)

# козы
goat_horns = Goat('Рога', 30)
goat_hooves = Goat('Копыта', 34)

print('Задача №1')
print('Животное:', duck.class_name, ' Имя:', duck.name + \
      '\nГолос:', duck.get_voice(), ' вес:', duck.weight, 'кг')
print('Животное:', goat_hooves.class_name, ' Имя:', goat_hooves.name + \
      '\nГолос:', goat_hooves.get_voice(), ' вес:', goat_hooves.weight, 'кг')


print('\nЗадача №2')
print(goat_horns.feed(),',', sheep_curly.feed())
print('Животное', sheep_curly.class_name, 'по имени', sheep_curly.name, 'и', sheep_barash.name,  'можно', sheep_curly.action())


print('\nЗадача №3')
print('Самое тяжелое животное зовут', Animals.max_weight_name, 'весит:', Animals.max_weight, 'кг')
print('Общий вес всех животных:', Animals.total_weight, 'кг')