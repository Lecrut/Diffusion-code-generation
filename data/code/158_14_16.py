EVEN_MASK = 1023

def get_even_numbers():
    even_numbers = []
    for num in range(100):
        if num & EVEN_MASK == 0:
            even_numbers.append(num)
    return sorted(even_numbers)
if __name__ == '__main__':
    print(get_even_numbers())