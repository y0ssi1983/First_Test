### Question number 5

first_num = int(input("please write any number: "))
second_num = int(input("please write any number: "))
if second_num != 0:
    print(first_num / second_num)
else:
    print("error")

### Question number 6

names1 = ["Eyal", "barak", "Moshe", "Elad", "eli"]
names2 = []

for x in names1:
    if "e" in x:
        names2.append(x)
print(names2)

### Question number 7

Messge = "M6y fir88302st84 a6ss89i32g35n456m23e08n57t"
result = ''.join([i for i in Messge if not i.isdigit()])
print(result)

### Question number 8 ----- I didn't success this Question

dict = {1: "yossi", 2: "elad", 3: "avi"}
def func(dict):
    for key in dict:
        return True

if func(dict) == 1:
    print("True")

### Question number 9
git config --global user.name "eyal golan"


### Question number 10
git reset --soft file1


### Question number 11
UPDATE GAMES SET CONUT = TYPE.ARCADE WHERE ID = 4;


### Question number 12
SELECT ID,NAME FROM PASSENGERS WHERE AGE < 9;



