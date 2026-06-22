def generate_feet_values():
    miles = (1, 5, 10, 50, 100)
    for mile in miles:
        yield mile * 5280

if __name__ == '__main__':
    generator = generate_feet_values()
    for feet in generator:
        print(feet)