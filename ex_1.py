def hello(a: str) -> str:
   
    return "Hello " + a


print("Example")
print(hello("Ola"))

assert hello("Ola") == "Hello Ola"
assert hello("Zuzia") == "Hello Zuzia"

print("Zadanie zrobione")