class LogicGate:
    GATE_TYPE = "AND"
    @staticmethod
    def get_gate_type():
        return LogicGate.GATE_TYPE
    def __init__(self):
        self._type = LogicGate.GATE_TYPE
    def process(self, in1, in2):
        if not isinstance(in1, bool) or not isinstance(in2, bool):
            raise ValueError("Inputs must be boolean")
        return bool(in1 and in2)

if __name__ == '__main__':
    gate = LogicGate()
    val1 = True
    val2 = False
    output = gate.process(val1, val2)
    print(output)