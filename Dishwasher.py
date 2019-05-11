class Dishwasher:
    amount = 0

    def __init__(self, costs_water_for_year=50000, number_of_programmes=12, brand="Bosch", quantity_of_dishes=50, producing_country="Germany", price=300, model="ZX"):
        self.costs_water_for_year = costs_water_for_year
        self.number_of_programmes = number_of_programmes
        self.brand = brand
        self.quantity_of_dishes = quantity_of_dishes
        self.producing_country = producing_country
        self.price = price
        self.model = model

    def __del__(self):
        return print(self.costs_water_for_year + 40000)

    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def get_static_field():
        return Dishwasher.amount

def main():
    default_dishwasher = Dishwasher()
    big_dishwasher = Dishwasher(35000, 10, "Whirpool", 45, price=200, model="XR")
    small_dishwasher = Dishwasher(30000, 8, "Philips", 40, price=250, model="None")

    print(default_dishwasher)
    print(big_dishwasher)
    print(small_dishwasher)
    print(Dishwasher.get_static_field())

if __name__ == "__main__":
    main()
