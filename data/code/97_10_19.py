class TruthTableGenerator:
    OPERATIONS = {
        "AND": lambda v1, v2: v1 and v2,
        "OR": lambda v1, v2: v1 or v2,
        "XOR": lambda v1, v2: v1 ^ v2,
        "NOT_V1": lambda v1, _: not v1,
        "NOT_V2": lambda _, v2: not v2
    }

    @staticmethod
    def generate_truth_table(operation_name):
        print(f"Truth Table for {operation_name}:")
        print("A | B | Result")
        print("---+---+--------")
        for a in [False, True]:
            for b in [False, True]:
                result = TruthTableGenerator.OPERATIONS.get(operation_name, lambda _, __: "Unknown Operation")(a, b)
                print(f"{a} | {b} | {result}")

if __name__ == '__main__':
    truth_table_generator = TruthTableGenerator()
    truth_table_generator.generate_truth_table("AND")