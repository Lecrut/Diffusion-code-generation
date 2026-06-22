import ast

INSTRUCTION_KEY = 'instruction'
COUNT_KEY = 'count'

def execute_instructions(instructions):
    for item in instructions:
        instruction = item[INSTRUCTION_KEY]
        count = item[COUNT_KEY]
        for _ in range(count):
            try:
                exec(instruction)
            except Exception as e:
                print(f"Error executing {instruction}: {e}")

if __name__ == '__main__':
    sample_instructions = [
        {'instruction': 'print("Hello")', 'count': 3},
        {'instruction': 'print("World")', 'count': 2}
    ]
    execute_instructions(sample_instructions)