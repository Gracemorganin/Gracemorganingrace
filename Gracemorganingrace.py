import datetime
import random

def generate_log_entry():
    now = datetime.datetime.now().isoformat()
    seed = random.randint(100000, 999999)
    return f"[AUTO LOG SCRIPT] {now} Seed: {seed}"

def write_log():
    with open("log.txt", "a") as f:
        for _ in range(5):
            f.write(generate_log_entry() + "\n")

if __name__ == "__main__":
    print("Запуск генератора логов...")
    write_log()
    print("Логи успешно записаны.")
