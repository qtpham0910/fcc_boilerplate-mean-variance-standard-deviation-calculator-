import numpy as np

def calculate(list):
  if len(list) == 9:
        list = np.array(list).reshape(3,3)
        calculations = {
            'mean': [np.mean(list, 0).tolist(),
                    np.mean(list, 1).tolist(),
                    np.mean(list)],
            'variance': [np.var(list, 0).tolist(),
                         np.var(list, 1).tolist(),
                         np.var(list)],
            'standard deviation': [np.std(list, 0).tolist(),
                                   np.std(list, 1).tolist(),
                                   np.std(list)],
            'max': [np.max(list, 0),
                    np.max(list, 1),
                    np.max(list)],
            'min': [np.min(list, 0),
                    np.min(list, 1),
                    np.min(list)],
            'sum': [np.sum(list, 0),
                    np.sum(list, 1),
                    np.sum(list)]
        }
        
  else:
      raise ValueError('List must contain nine numbers.')
  return calculations