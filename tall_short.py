from sklearn.tree import DecisionTreeClassifier


x = [[150], [160], [170], [180], [190]]


y = ["short", "short", "tall", "tall", "tall"]


model = DecisionTreeClassifier()

model.fit(x, y)


print("Your height is:", model.predict([[160]])[0])

print("Your height is:", model.predict([[180]])[0])
