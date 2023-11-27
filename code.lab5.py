class Musician:
    def __init__(self, name, fee, age):
        self.name = name
        self.fee = fee
        self.age = age

    def __str__(self):
        return f"{self.name} (Age: {self.age}, Fee: {self.fee})"

class MusicFestival:
    def __init__(self, max_budget):
        self.max_budget = max_budget
        self.musicians = []

    def add_musician(self, musician):
        if self.calculate_total_fee() + musician.fee <= self.max_budget:
            self.musicians.append(musician)
            print(f"{musician.name} додано до фестивалю.")
        else:
            print(f"{musician.name} не може бути доданий до фестивалю через перевищення бюджету.")

    def remove_musician(self, musician):
        if musician in self.musicians:
            self.musicians.remove(musician)
            print(f"{musician.name} видалено з фестивалю.")
        else:
            print(f"{musician.name} не знайдено на фестивалі.")

    def calculate_total_fee(self):
        return sum(musician.fee for musician in self.musicians)

    def all_musicians(self):
        print("Виконавці на фестивалі зараз:")
        for musician in self.musicians:
            print(musician)


if __name__ == "__main__":
    festival = MusicFestival(21000)

    musician1 = Musician("Перший виконавець", 5000, 30)
    musician2 = Musician("Другий виконавець", 6000, 25)
    musician3 = Musician("Третій виконавець", 3000, 21)

    print(f":" * 41)

    festival.add_musician(musician1)
    festival.add_musician(musician2)
    festival.add_musician(musician3)

    print(f":" * 41)
    festival.all_musicians()
    print(f":" * 41)

    musician4 = Musician("Четвертий виконавець", 7000, 24)
    festival.add_musician(musician4)
    festival.remove_musician(musician1)

    print(f":" * 41)
    festival.all_musicians()
    print(f":" * 41)