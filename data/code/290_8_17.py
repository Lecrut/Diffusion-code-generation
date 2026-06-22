class MassConverter:
    KG_TO_TONS = 0.001

    @staticmethod
    def kg_to_tons(kg):
        return round(kg * MassConverter.KG_TO_TONS, 3)

if __name__ == '__main__':
    sample_kg = 5000
    tons = MassConverter.kg_to_tons(sample_kg)
    print(f"{tons} tons")