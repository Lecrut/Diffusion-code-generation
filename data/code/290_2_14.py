class MassConverter:
    KILO_TO_POUND = 0.453592

    @staticmethod
    def tons_to_kg(tons):
        return int(tons * 1000)

if __name__ == '__main__':
    tons_value = 2
    kg_value = MassConverter.tons_to_kg(tons_value)
    print(f"{tons_value} tons is {kg_value} kg")