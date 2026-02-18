class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    new_persons = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        new_person = list(filter((lambda n_person: n_person.name == person["name"]), new_persons))[0]
        if "wife" in person.keys() and person.get("wife"):
            wife = list(filter((lambda n_person: n_person.name == person.get("wife")), new_persons))[0]
            new_person.wife = wife
        if "husband" in person.keys() and person.get("husband"):
            husband = list(filter((lambda n_person: n_person.name == person.get("husband")), new_persons))[0]
            new_person.husband = husband

    return new_persons
