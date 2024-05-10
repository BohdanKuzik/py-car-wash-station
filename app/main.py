class Car:
    def __init__(
            self,
            comfort_class: float,
            clean_mark: float,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: float,
            average_rating: float,
            count_of_ratings: float
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (
                (car.comfort_class * (self.clean_power - car.clean_mark)
                 ) * (self.average_rating / self.distance_from_city_center)
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = (total_rating + rating) / self.count_of_ratings
        self.average_rating = round(self.average_rating, 1)


bmw = Car(3, 3, "BMW")
audi = Car(4, 9, "Audi")
mercedes = Car(7, 1, "Mercedes")

wash_station = CarWashStation(6, 8, 3.9, 11)

income = wash_station.serve_cars([bmw, audi, mercedes])
print(income)

wash_cost = wash_station.calculate_washing_price(Car(2, 1, "Ford"))
print(wash_cost)

wash_station.rate_service(5)
print(wash_station.count_of_ratings)
print(wash_station.average_rating)
