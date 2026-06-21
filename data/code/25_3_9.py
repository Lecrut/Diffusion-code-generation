def apply_discount(price):
    if price > 100:
        return price * 0.9
    else:
        return price * 0.95

if __name__ == '__main__':
    print(apply_discount(50))
    print(apply_discount(150))