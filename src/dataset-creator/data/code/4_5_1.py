import asyncio
from typing import List, Dict, Any
async def process_branch_a(data: str) -> Dict[str, Any]:
    return {"branch": "A", "status": "completed", "data_length": len(data)}
async def process_branch_b(data: int) -> Dict[str, Any]:
    if data > 100:
        result = f"Value {data} exceeds threshold."
    else:
        result = f"Value {data} is within range."
    return {"branch": "B", "status": "completed", "message": result}
async def process_branch_c(data: float) -> Dict[str, Any]:
    squared = data ** 2
    return {"branch": "C", "status": "completed", "squared_value": squared}
async def main():
    tasks: List[Dict[str, Any]] = [
        {
            "input_type": "string",
            "value": "Hello World",
            "handler": process_branch_a,
        },
        {
            "input_type": "int",
            "value": 150,
            "handler": process_branch_b,
        },
        {
            "input_type": "float",
            "value": 4.2,
            "handler": process_branch_c,
        },
    ]
    results = await asyncio.gather(*[task["handler"](task["value"]) for task in tasks])
    print("Results:")
    for result in results:
        print(result)
if __name__ == '__main__':
    asyncio.run(main())