conversion_factors = {
    'hours': 3600 * 1000
}

def hours_to_milliseconds(hours):
    return int(hours * conversion_factors['hours'])

if __name__ == '__main__':
    print(hours_to_milliseconds(2))
    print(hours_to_milliseconds(5))