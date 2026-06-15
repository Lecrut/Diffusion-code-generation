class Instruction:
    def __init__(self, name, action):
        self.name = name
        self.action = action
class RepetitionRule:
    def __init__(self, condition, repetition_count, repetition_type):
        self.condition = condition
        self.repetition_count = repetition_count
        self.repetition_type = repetition_type
class InstructionSet:
    def __init__(self, instructions):
        self.instructions = instructions
class RepetitionEngine:
    def __init__(self, rules):
        self.rules = rules
    def execute(self, instruction, context):
        if not self.rules:
            return instruction.action
        for rule in self.rules:
            if instruction.action == rule.condition:
                result = ""
                for _ in range(rule.repetition_count):
                    result += f"Repeat: {instruction.name} -> {instruction.action}\n"
                return result
        return instruction.action
if __name__ == '__main__':
    sample_instructions = [
        Instruction("increment", "add 1 to value"),
        Instruction("print", "display current value")
    ]
    sample_rules = [
        RepetitionRule("add 1 to value", 3, "count"),
        RepetitionRule("display current value", 2, "repeat_action")
    ]
    instruction_set = InstructionSet(sample_instructions)
    repetition_engine = RepetitionEngine(sample_rules)
    initial_context = {"value": 10}
    current_context = initial_context.copy()
    print("--- Execution Start ---")
    for instruction in sample_instructions:
        print(f"\nExecuting Instruction: {instruction.name}")
        if instruction.action == "add 1 to value":
            current_context["value"] += 1
        elif instruction.action == "display current value":
            print(f"Result: {current_context['value']}")
        output = repetition_engine.execute(instruction, current_context)
        if output:
            print("Repetition Output:")
            print(output)
    print("\n--- Execution End ---")