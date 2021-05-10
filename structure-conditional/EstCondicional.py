def muestraMenorEdad():
  #Definir variables y otros
  pnombre=""
  pedad=0
  #datos de entrada
  p1nombre=input("ingrese nombre 1ra persona:")
  p1edad=int(input("ingrese edad 1ra persona:"))
  p2nombre=input("ingrese nombre 2ra persona:")
  p2edad=int(input("ingrese edad 2ra persona:"))
  p3nombre=input("ingrese nombre 3ra persona:")
  p3edad=int(input("ingrese edad 3ra persona:"))
  #proceso
  if p1edad<p2edad and p1edad<p3edad:
    pnombre=p1nombre
    pedad=p1edad
  elif p2edad<p1edad and p2edad<p3edad:
    pnombre=p2nombre
    pedad=p2edad
  else:
    pnombre=p3nombre
    pedad=p3edad
  #Datos de salida
  print("la persona con menor edad es:", pnombre, "y su edad es:", pedad)

muestraMenorEdad()
  