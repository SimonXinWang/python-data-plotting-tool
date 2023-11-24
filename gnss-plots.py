#!/usr/bin/python3.6

"""
  **************************************************************************************************
  * @file    crc_utility.py
  * @author  Genesys Electronics Design Team
  * @version V1.0.0
  * @date    14-Apr-21
  * @brief   This module is used for performing the cyclic redundancy check algorithm.
  *
  @verbatim
  **************************************************************************************************
   Copyright (c) 2023, Simon Wang
   All Rights Reserved

   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
   IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
   FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
   DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
   DATA, OR PROFITS OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
   IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
   OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  **************************************************************************************************
    Revision Number     : 1.0.0
    Revision By         : 
    Date                : 24-Nov-23
    Description         : 
  **************************************************************************************************
"""
import numpy as np
import matplotlib.pyplot as plt

# CRC polynomials
CRC_UTILITY__CRC_8_CCITT_NORMAL = 0x07
CRC_UTILITY__CRC_8_CCITT_REVERSED = 0xE0
CRC_UTILITY__CRC_8_TH_SHT4X = 0x31

# Error Codes
CRC_UTILITY__ERROR_INVALID_PARAMETER = 2


# @brief    Function to calculate CRC8 checksum of given data, least significant bit first,
#           both in terms of the algorithm and the polynomial to be used,
#           which is the so called "reverse polynomial". The reverse polynomial
#           CRC_UTILITY__CRC_8_CCITT_REVERSED should be used as crc_polynomial parameter.
# @param    data_ro         - buffer containing the data
# @param    crc_polynomial  - To use for CRC Calculation
# @return   error           - error result of funciton
# @return   crc_accumulator - CRC value result
#

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)


# plotting
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()


#
# CRC calc for TempHumidity Sensor samples
#
print("CRC8 for real samples")
error, crc = calculate_crc8_lsb([0x10, 0xC5], CRC_UTILITY__CRC_8_TH_SHT4X)
print(hex(crc))
print("error is:", error)


print("CRC8 for example")
error, crc = calculate_crc8_lsb([0xEF, 0xBF], CRC_UTILITY__CRC_8_TH_SHT4X)
print(hex(crc))
error, crc = calculate_crc8_lsb([0xBF, 0xEF], CRC_UTILITY__CRC_8_TH_SHT4X)
print(hex(crc))
error, crc = calculate_crc8_lsb(
    [0xBF, 0xEF], CRC_UTILITY__CRC_8_CCITT_REVERSED)
print(hex(crc))

print("created my own exercise Git repository for practice python")
print("---------------------------------------------")
#
# verify CRC result by inserting the result into end of data array
#
print(calculate_crc16([0, 1, 2, 1, 0, 1, 0, 0, 0xC61B]))

print("Simon tried himself here")
print(hex(calculate_crc16([0x00, 0x01, 0x02, 4, 0, 1, 0, 0])))


#
# all data are in Hex
#
print('Hex of Caclulated CRC16:', hex(calculate_crc16(
    [0x7E, 0x10, 0x00, 0x01, 0x02, 0x01, 0x00, 0x01, 0x00, 0x00, 0x1B, 0xC6])))

#
# all data are in decimal
#
print('Caclulated CRC16 in decimal:', calculate_crc16(
    [0, 1, 2, 1, 0, 1, 0, 0, 125, 1782]))

