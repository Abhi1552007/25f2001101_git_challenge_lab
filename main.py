# main.py
from sum_module import add
from diff_module import subtract

def main():
    a, b = 10, 3
    print("a + b =", add(a, b))
    print("a - b =", subtract(a, b))

if __name__ == "__main__":
    main()
