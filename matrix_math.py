class ShapeException(Exception):
    pass
m = [3, 4 ,5]
n = [5, 0, 1]
z = [9,8]
w = [0, 2, 4]
y = [10, 20, 30]


def shape_of(vec1):
    if type(vec1[0])==int:
        return (len(vec1),)
    else:
        return(len(vec1),len(vec1[1]))

def shape_vectors(x):
    return (len(x), )


def vector_add(vec1, vec2):
    if shape_of(vec1)!=shape_of(vec2):
        raise ShapeException()
    return [(vec1[i]+vec2[i]) for i in range(len(vec1))]




def vector_add_is_communicative(vec1, vec2):
     if vector_add(vec1,vec2) == vector_add(vec2,vec1):
         return True


def vector_sub(vec1,vec2):
    if shape_of(vec1)!=shape_of(vec2):
        raise ShapeException()
    return [(vec1[i]-vec2[i]) for i in range(len(vec1))]


def vector_sum(*vectors):
    vec_len = len(vectors[1])
    for i in vectors:
        if len(i)!=vec_len:
            raise ShapeException()
    return [sum(i) for i in zip(*vectors)]

def dot(vec1,vec2):
    if shape_of(vec1)!=shape_of(vec2):
        raise ShapeException()
    return sum([(vec1[i]*vec2[i]) for i in range(len(vec1))])

def vector_multiply(vec1, scalar):
    return [vec1[i] * scalar for i in range(len(vec1))]
