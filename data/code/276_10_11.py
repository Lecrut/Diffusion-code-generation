def repeat_instructions(instructions, count):
    for instruction in instructions:
        for _ in range(count):
            print(instruction)

if __name__ == '__main__':
    sample_instructions = [
        "Prepare the ingredients",
        "Mix them thoroughly",
        "Bake at 350 degrees for 20 minutes"
    ]
    repeat_instructions(sample_instructions, 3)