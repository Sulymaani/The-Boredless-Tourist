destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Cairo, Egypt", ["historical site", "art"]]


def get_destination_index(destination):
    for index in destinations:
        if index == destination:
            destination_index = 0
            destination_index += destinations.index(index)
            return destination_index


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# print(get_destination_index("Los Angeles, USA"))
