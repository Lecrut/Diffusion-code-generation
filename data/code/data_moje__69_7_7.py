def feet_generator(mile_tuple):
    for mile in mile_tuple:
        yield mile * 5280

if __name__ == '__main__':
    distances = (1, 5, 10, 26)
    for feet in feet_generator(distances):
        print(feet)