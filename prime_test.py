import sys

# Change this number to control Jenkins build result
num = 4# Success if prime, failure if not

# Prime check logic
if num < 2:
    print(f"ERROR: {num} is not a prime number.")
    sys.exit(1)

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print(f"ERROR: {num} is not a prime number.")
        sys.exit(1)

print(f"{num} is a prime number. Build succeeded.")
sys.exit(0)
