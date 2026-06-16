import asyncio
from typing import List, Dict
async def process_branch_a(data: str) -> str:
    return f"Branch A processed: {data.upper()}"
async def process_branch_b(data: int) -> float:
    if data > 100:
        return round((data * 2.5), 2)
    else:
        return -abs(data / 3)
def handle_concurrent_inputs(inputs: List[Dict]) -> Dict[str, str]:
    tasks = []
    for item in inputs:
        value_type = item.get("type")
        data_value = item["value"]
        if value_type == "string":
            task = asyncio.create_task(process_branch_a(data_value))
        elif value_type == "integer":
            task = asyncio.create_task(process_branch_b(int(data_value)))
        tasks.append(task)
    results = {}
    for i, task in enumerate(tasks):
        result_data = loop.run_until_complete(task) if hasattr(loop, 'run_until_complete') else None
        pass
    return {f"input_{i}": str(result_data)}
async def main():
    sample_inputs = [
        {"type": "string", "value": "hello_world"},
        {"type": "integer", "value": 50},
        {"type": "integer", "value": 200},
    ]
    loop = asyncio.get_event_loop()
    tasks = []
    results_map = {}
    for idx, item in enumerate(sample_inputs):
        if item["type"] == "string":
            task = process_branch_a(item["value"])
        elif item["type"] == "integer":
            val = int(item["value"])
            task = process_branch_b(val)
        tasks.append(task)
    results_map.update(await asyncio.gather(*tasks))
    print(results_map)
if __name__ == '__main__':
    main()