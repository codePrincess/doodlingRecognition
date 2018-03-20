from coremltools.converters import sklearn as sklearn_to_ml
from sklearn.externals import joblib

model = joblib.load('mymodel.pkl')

print('Converting model')
coreml_model = sklearn_to_ml.convert(model)

print('Saving CoreML model')
coreml_model.save('mycoremlmodel.mlmodel')