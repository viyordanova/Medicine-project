class Medicine:
    def __init__(self,med_id, med_name, manufacturer, price, quantity):
        self.id = med_id
        self.name = med_name
        self.manufacturer = manufacturer
        self.price = price 
        self.quantity = quantity

    def Display(self):
        print(f'Info: {self.name} {self.id} {self.manufacturer} {self.price} {self.quantity}')

    def Search_by_name(self, name):
        if name == self.name:
            self.Display()
        else:
            print("Не е намерено такова лекарство.")

    def Sale(self):
        quantity = int(input(f'Колко искате да продадете от {self.name}:'))
        self.quantity = quantity
        print(f'Новото количество от {self.name} е {self.quantity}')
        profit = quantity * self.price
        print(f'Продадохте стока на стойност: {profit} лв.')

    def Purchase(self):
        quantity = int(input(f'Колко искате да заредите от {self.name}: '))
        self.quantity += quantity
        print(f'Новото количество от {self.name} е {self.quantity}')
        expense = quantity * self.price
        print(f'Закупеното количество е на цена:{expense} лв.')

meds =[
    Medicine(101,"Aspirin", "AA",10,20),
    Medicine(102,"Ibuprofen", "AA",15,30),
    Medicine(103,"Paracetamol", "AA",12,42),
    Medicine(104,"Analgin", "AA",100,16),
]

try:
    number_of_meds = int(input('Колко лекарства искате да въведете: '))
except ValueError:
    print('Трябва да въведете число. ')
try:
    for i in range(number_of_meds):
        print(f'\n Medicament{i+1}/{number_of_meds}')
        try:
            med = Medicine(int(input('10: ')),input('Name: '),input('Manufacturer: '),int(input('Price: ')),int(input('Quantity: ')))
            meds.append(med)
        except ValueError:
            print('Не попълвате информацията правилно.')
            break
except NameError:
    print('И това трябваше да е число ама :/ ')

def Sort_Meds():
    meds.sort(key=lambda med:meds.name)
    print('Medicaments sorted by name:\n')
    for i in meds:
        i.Display()

Sort_Meds()