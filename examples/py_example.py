from PIL import Image
from bs4 import BeautifulSoup
import requests
from pandas import DataFrame
from dataclasses import dataclass


model_14 = DataFrame

x -> int

class Car:
    class_attributes = "value"

    def __init__(self, name, color, model_no, price):
        # creating instances
        self.name = name
        self.model_no = model_no
        self.color = color
        self.price = price

    def car_details(self):
        return f"Car name : {self.name} \nCar Model: {self.model_no} \nCar Color: {self.color} \nCar Price: {self.price}"


Car1 = Car("BMW", "Blue", "101", "100000")
print(f"Car details: {Car1.car_details()}")


n = int(2.2)
xxxx = list(2, 5, 746, 35, 87, 234, 654)


def myfunc(n):
    return lambda x: x * n


# doubler becomes the name of the otherwise anonymous lambda
# so doubler literally becomes lambda x: x * 2
# assigning myfunc(2) to doubler assigns 2 to n in the lambda
doubler = myfunc(2)  # => lambda x: x * 2

# calling doubler in print then calls the lambda and assigns 2 to x
# so becomes lambda 2 * 2, which implicitly returns the result of 4
print(doubler(2))  # => 2 * 2 = 4


url = "https://en.wikipedia.org/wiki/Algorithm"


res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
for href in soup.find_all("a"):
    print(href["href"])


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog = Animal("Tom", 14)

kk = [1, 2, 3, 4, 5]
new_kk = kk.append(100)
print(new_kk)

kk = (1, 2, 3, 4, 5)
kk = list(kk)
kk.append(100)
new_kk = tuple(kk)
print(new_kk)

tup = (1, 3, 5)
y = (4,)
tup += y
print(tup)


class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("run")


player1 = PlayerCharacter("cindy")
# print(player1.run)

player1.run()


image = Image.open(r"C:\Users\pablo\OneDrive\Escritorio\remera.jpg")
new_image = image.resize((28, 28))
pred_probs = model_14.predict((new_image))
print(pred_probs)
"text string"

tup = 1, 2, 3, 4
print(tup)

print(int(4.78e07))

tup = (7, 14, 21)
tup1 = tup + (28,)
tup2 = tup * 3

print(tup1, tup2, sep="\n")


@dataclass
class Greet:
    greets: tuple
    nick: str

x = "Hey Fuckers!"
y = False
if x == y:
    raise TypeError


class IterGreets:
    x = 6

    def __init__(self, greet: Greet) -> None:
        self.greet = greet

    def iter(self):
        self.count = -1
        return self

    def next(self):
        self.count += 1
        if self.count < len(self.greet.greets):
            return f"{self.greet.greets[self.count]} {self.greet.nick}"
        else:
            raise StopIteration


greet_dbclick = Greet(nick="dbclick", greets=("Hi", "Hello", "Nice to meet you to"))

for greet in IterGreets(greet_dbclick):
    print(greet)


rows = [[1], [1, 1]]


def recurse_rowIndex(rowIndex: int):
    if rowIndex > len(rows):
        recurse_rowIndex(rowIndex - 1)
    if rowIndex == len(rows):
        rows.append([1])
        for val in range(1, rowIndex):
            rows[rowIndex].append(rows[rowIndex - 1][val - 1] + rows[rowIndex - 1][val])
        rows[rowIndex].append(1)
    return rows[rowIndex]


print(recurse_rowIndex(33))


def math_rowIndex(rowIndex: int):
    previous = 1
    count = 1
    nth_row = [1]

    while count <= rowIndex:
        current = (previous * (rowIndex - count + 1)) // count
        previous = current
        count += 1
        nth_row.append(current)

    return nth_row


print(math_rowIndex(33))
print(math_rowIndex(33) == recurse_rowIndex(33))
