print("Hello world")
def add(x,y):
    return x+y,

def subtract(x,y):
    return x -y,

#list example
numbers=[1,2,3,4]
squares=[x**2 for x in numbers if x%2 ==0]
print(squares)

#dictionary example
d={'cat':4,'bird':2,'snake':0}
for animals,legs in d.items():
    print(f"The {animals} has {legs} legs")

    def evensquares():
        x=(int(input('Enter a number:')))
        if x **2 %2 ==0:
            print('The answer is even') 
        else: print('The answer is odd')
evensquares(),

