def tons_to_kg(tons):
    return int(tons * 1000)

if __name__ == '__main__':
    tons_value = 3.5
    kg_value = tons_to_kg(tons_value)
    print(f"{tons_value} tons is {kg_value} kg")