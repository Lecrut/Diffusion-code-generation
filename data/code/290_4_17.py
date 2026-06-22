def pounds_to_kilograms(pounds):
    if pounds < 0:
        return 'Invalid input'
    elif pounds == 0:
        return 0.0
    else:
        kilograms = pounds * 0.453592
        return round(kilograms, 1)
if __name__ == '__main__':
    print(pounds_to_kilograms(10))