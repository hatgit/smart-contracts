import Config


from Common.Utils.UserInput import read
from Common.ModelCalculatorComparePythonAndSolidity import run
from Common.ModelCalculatorWrapper import ConvertN2R as conversionHandler
from Common.Utils.InputGenerator import getRandomDistribution as distributionFunc


run(read(default=1000),Config.Logger(),conversionHandler,distributionFunc)