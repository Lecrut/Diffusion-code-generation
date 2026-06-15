import sys
def generate_powers_of_two():
    n = 30
    current_power = 1
    for i in range(n + 1):
        print(current_power)
        current_power <<= 1
if __name__ == '__main__':
    generate_powers_of_two()