def functionA():
    print("A1")
    from foo2 import functionB
    print("A2")
    functionB()
    print("A3")

def functionB():
    print("b1")


print("t1")

if __name__ == "__main__":
    print("m1")
    functionA()
    print("m2")

print("t2")