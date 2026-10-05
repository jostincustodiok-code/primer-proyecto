#-----------REGISTRO DE PRODUCTOS----------------


#lista de todos los productos

productos=[]


def registrar_producto():
   print("REGISTRO DE PRODUCTOS")
print("-"*35)



nombre=input("ingrese el nombre del productos:")
precio=float(input("ingrese el precio del producto:"))
cantidad=int(input("ingrese la cantidad del producto:"))
categoria=input("ingrese la categoria del producto:")
variedades=int(input("ingrese la cantidad de variedades del producto:"))


producto={

"nombre": nombre,
"precio": precio,
"cantidad": cantidad,
"categoria": categoria,
"variedades": variedades,
}


print("\n==========PRODUCTOS REGISTRADO============")

print("nombre del producto:", producto["nombre"])
print("precio del producto:", producto["precio"])
print("cantidad del producto:", producto["cantidad"])
print("categoria del producto:", producto["categoria"])
print("cantidad de variedades del producto:",producto["variedades"])



