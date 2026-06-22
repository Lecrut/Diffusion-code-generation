def feet_to_inches(feet):
    return int(feet * 12) if feet == int(feet) else float(feet * 12)

if __name__ == '__main__':
    print(feet_to_inches(5))
    print(feet_to_inches(2.5))