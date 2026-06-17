class Instruction:
    def __init__(self, instruction_type, parameters):
        self.instruction_type = instruction_type
        self.parameters = parameters
class RepetitionRule:
    def __init__(self, condition, repetition_count, action):
        self.condition = condition
        self.repetition_count = repetition_count
        self.action = action
class InstructionRepeter:
    def __init__(self, rules):
        self.rules = rules
    def execute(self, instructions):
        results = []
        for instruction in instructions:
            for rule in self.rules:
                if self._check_condition(instruction, rule.condition):
                    for i in range(rule.repetition_count):
                        result = self._apply_action(instruction, rule.action, i)
                        results.append(result)
        return results
    def _check_condition(self, instruction, condition):
        if condition == "always":
            return True
        if condition == "if_true":
            return bool(instruction.parameters.get('value', False))
        return False
    def _apply_action(self, instruction, action, index):
        if action == "print":
            return f"Repeated execution of {instruction.instruction_type} (Index: {index})"
        elif action == "modify":
            new_value = instruction.parameters.get('value', 0) + index
            instruction.parameters['value'] = new_value
            return f"Modified {instruction.instruction_type} to {new_value}"
        else:
            return f"Unknown action: {action}"
if __name__ == '__main__':
    sample_instructions = [
        Instruction("ADD", {"value": 10}),
        Instruction("MULTIPLY", {"value": 5}),
        Instruction("SUBTRACT", {"value": 20})
    ]
    repetition_rules = [
        RepetitionRule(condition="always", repetition_count=3, action="print"),
        RepetitionRule(condition="if_true", repetition_count=2, action="modify")
    ]
    reputer = InstructionRepeter(repetition_rules)
    final_results = reputer.execute(sample_instructions)
    for result in final_results:
        print(result)