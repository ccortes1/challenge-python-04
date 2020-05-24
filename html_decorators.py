def div(func):
    def wrapper(*args, **kwargs):
        funci = func(*args, **kwargs)
        print(f"<div>{funci}</div>")
        return funci
    return wrapper

def article(func):
    def wrapper(*args, **kwargs):
       funci = func(*args, **kwargs)
       print(f"<article>{funci}</article>")
       return funci
    return wrapper

def p(func):
    def wrapper(*args, **kwargs):
       funci = func(*args, **kwargs)
       print(f"<p>{funci}</p>")
       
    return wrapper


# Here you must apply the decorators, uncomment this later
@p
@article
@div 
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'

def run():
    saludo('Jorge')


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
